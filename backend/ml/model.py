"""
ML Model Adapter — SymptoCare Backend

This module wraps the original RandomForest model logic from the research
repository (final.py / Prediction.py) into a clean, API-friendly interface.

Key design decisions:
  - Model trains ONCE at module import time (singleton pattern).
  - Exact same preprocessing pipeline as the original code is preserved.
  - predict() accepts a list of symptom name strings (not raw weights).
  - Returns disease, specialist, and a confidence score.
"""

import os
import warnings
import logging
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Suppress pandas FutureWarnings from the original preprocessing pipeline
warnings.filterwarnings("ignore", category=FutureWarning, module="pandas")

from config import config

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Module-level singletons (trained once, reused for all requests)
# ---------------------------------------------------------------------------
_rf_model: RandomForestClassifier | None = None
_symptom_weights: dict[str, float] = {}        # symptom_name -> weight
_disease_specialist_map: dict[str, str] = {}   # disease -> specialist
_disease_description_map: dict[str, str] = {}  # disease -> description
_disease_precaution_map: dict[str, list] = {}  # disease -> [precaution...]
_known_symptoms: list[str] = []                # canonical symptom names


def _load_and_train() -> None:
    """
    Replicates the exact preprocessing + training pipeline from final.py.
    Called once at module import. Results cached in module-level singletons.
    """
    global _rf_model, _symptom_weights, _disease_specialist_map
    global _disease_description_map, _disease_precaution_map, _known_symptoms

    logger.info("SymptoCare ML: Loading CSV datasets...")

    # --- Load Symptom.csv (main training data) ---
    symptom_csv = os.path.join(config.DATA_DIR, config.SYMPTOM_CSV)
    df = pd.read_csv(symptom_csv)

    # Drop columns Symptom_6..17 (as in original — too many nulls)
    cols_to_drop = [
        "Symptom_6", "Symptom_7", "Symptom_8", "Symptom_9", "Symptom_10",
        "Symptom_11", "Symptom_12", "Symptom_13", "Symptom_14", "Symptom_15",
        "Symptom_16", "Symptom_17",
    ]
    df.drop(cols_to_drop, axis=1, inplace=True)

    # Clean whitespace across all cells (as in original)
    cols = df.columns
    data_flat = df[cols].values.flatten()
    s = pd.Series(data_flat)
    s = s.str.strip()
    s = s.values.reshape(df.shape)
    df = pd.DataFrame(s, columns=cols)
    df = df.fillna(0)
    vals = df.values

    # --- Load Symptom Severity.csv (provides weight values) ---
    severity_csv = os.path.join(config.DATA_DIR, config.SEVERITY_CSV)
    df1 = pd.read_csv(severity_csv)
    
    # Build symptom → weight lookup for the prediction function
    for _, row in df1.iterrows():
        _symptom_weights[str(row["Symptom"]).strip()] = float(row["weight"])

    _known_symptoms = sorted(_symptom_weights.keys())
    symptom_to_index = {symptom: i for i, symptom in enumerate(_known_symptoms)}

    # Convert training data to one-hot encoded binary vectors
    X_list = []
    y_list = []
    
    for _, row in df.iterrows():
        vec = np.zeros(len(_known_symptoms), dtype=int)
        for val in row[1:]:
            sym = str(val).strip()
            if sym in symptom_to_index:
                vec[symptom_to_index[sym]] = 1
        X_list.append(vec)
        y_list.append(row["Disease"])
        
    X = np.array(X_list)
    y = np.array(y_list)

    # --- Train RandomForest (same params as original) ---
    logger.info("SymptoCare ML: Training RandomForest model (100 estimators)...")
    
    # Calculate accuracy on a split for logging purposes
    x_train, x_test, y_train, y_test = train_test_split(
        X, y,
        test_size=config.RF_TEST_SIZE,
        random_state=config.RF_RANDOM_STATE,
    )
    rf_eval = RandomForestClassifier(n_estimators=config.RF_N_ESTIMATORS, random_state=config.RF_RANDOM_STATE)
    rf_eval.fit(x_train, y_train)
    acc = rf_eval.score(x_test, y_test)
    logger.info(f"SymptoCare ML: Model ready. Test accuracy = {acc * 100:.2f}%")
    
    # Train the actual production model on the FULL dataset
    rf = RandomForestClassifier(n_estimators=config.RF_N_ESTIMATORS, random_state=config.RF_RANDOM_STATE)
    rf.fit(X, y)
    _rf_model = rf

    # --- Load Disease Specialist.csv ---
    specialist_csv = os.path.join(config.DATA_DIR, config.SPECIALIST_CSV)
    df2 = pd.read_csv(specialist_csv)
    for _, row in df2.iterrows():
        _disease_specialist_map[str(row["Disease"]).strip()] = str(
            row["Specialist"]
        ).strip()

    # --- Load Disease Description.csv ---
    description_csv = os.path.join(config.DATA_DIR, config.DESCRIPTION_CSV)
    df3 = pd.read_csv(description_csv)
    for _, row in df3.iterrows():
        _disease_description_map[str(row["Disease"]).strip()] = str(
            row["Description"]
        ).strip()

    # --- Load Symptom Precaution.csv ---
    precaution_csv = os.path.join(config.DATA_DIR, config.PRECAUTION_CSV)
    df4 = pd.read_csv(precaution_csv)
    for _, row in df4.iterrows():
        disease = str(row["Disease"]).strip()
        precautions = [
            str(row[col]).strip()
            for col in ["Precaution_1", "Precaution_2", "Precaution_3", "Precaution_4"]
            if pd.notna(row[col]) and str(row[col]).strip() not in ("", "nan")
        ]
        _disease_precaution_map[disease] = precautions

    logger.info(
        f"SymptoCare ML: Loaded {len(_known_symptoms)} symptoms, "
        f"{len(_disease_specialist_map)} diseases, "
        f"{len(_disease_specialist_map)} specialist mappings."
    )


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def get_known_symptoms() -> list[str]:
    """Return sorted list of all symptom names the model understands."""
    return _known_symptoms.copy()


def get_symptom_weight(symptom_name: str) -> float | None:
    """Return the numeric weight for a given symptom, or None if unknown."""
    return _symptom_weights.get(symptom_name.strip())


def get_specialist_for_disease(disease: str) -> str:
    """Return the specialist category for a given disease name."""
    return _disease_specialist_map.get(disease.strip(), "General Practitioner")


def get_disease_description(disease: str) -> str:
    """Return the description of a given disease."""
    return _disease_description_map.get(disease.strip(), "")


def get_disease_precautions(disease: str) -> list[str]:
    """Return the list of precautions for a given disease."""
    return _disease_precaution_map.get(disease.strip(), [])


def predict(symptom_names: list[str]) -> dict:
    """
    Predict disease and specialist from a list of normalized symptom names.

    Args:
        symptom_names: List of 1–5 canonical symptom name strings
                       (e.g., ["headache", "fever", "fatigue"])

    Returns:
        {
            "disease": str,
            "specialist": str,
            "confidence": float,      # 0.0 – 1.0
            "description": str,
            "precautions": list[str],
            "severity_score": int,    # sum of symptom weights
        }

    Raises:
        RuntimeError: if model has not been initialized.
    """
    if _rf_model is None:
        raise RuntimeError("ML model not initialized. Call _load_and_train() first.")

    normalized_symptoms = [s.strip() for s in symptom_names]

    # Create one-hot encoded input vector
    input_arr = np.zeros((1, len(_known_symptoms)), dtype=int)
    for sym in normalized_symptoms:
        if sym in _known_symptoms:
            idx = _known_symptoms.index(sym)
            input_arr[0, idx] = 1

    predicted_disease = _rf_model.predict(input_arr)[0]

    # Calculate severity score (still uses weights)
    weights = []
    for sym in normalized_symptoms:
        w = get_symptom_weight(sym)
        if w is not None:
            weights.append(w)
            
    severity_total = sum(weights)

    # Get probability for confidence score
    proba = _rf_model.predict_proba(input_arr)[0]
    confidence = float(max(proba))

    specialist = get_specialist_for_disease(predicted_disease)
    description = get_disease_description(predicted_disease)
    precautions = get_disease_precautions(predicted_disease)

    # Severity level label
    avg_severity = severity_total / max(len(symptom_names), 1)
    if avg_severity >= 6:
        severity_label = "high"
    elif avg_severity >= 4:
        severity_label = "medium"
    else:
        severity_label = "low"

    return {
        "disease": predicted_disease,
        "specialist": specialist,
        "confidence": round(confidence, 4),
        "description": description,
        "precautions": precautions,
        "severity_score": int(severity_total),
        "severity_level": severity_label,
    }


# ---------------------------------------------------------------------------
# Initialize model at import time
# ---------------------------------------------------------------------------
_load_and_train()
