"""
Prediction Service — SymptoCare Backend

Orchestrates the full symptom → disease → specialist pipeline:
  1. Accepts either natural language text OR a list of symptom names
  2. Routes to NLP service (text) or normalization (icon-based)
  3. Calls the ML model for prediction
  4. Returns a rich response with disease, specialist, confidence, precautions
"""

from __future__ import annotations
import logging
from typing import Optional

from ml import model as ml_model
from ml.symptom_encoder import build_symptom_metadata
from services.nlp_service import extract_symptoms, normalize_icon_symptoms
from config import config

logger = logging.getLogger(__name__)


class PredictionError(Exception):
    """Raised when prediction cannot be performed."""
    pass


def analyze_from_text(message: str) -> dict:
    """
    Process a natural language symptom message and predict disease/specialist.

    Args:
        message: Free-form text like "I have chest pain and trouble breathing"

    Returns:
        Full prediction response dict

    Raises:
        PredictionError: if no symptoms could be extracted
    """
    if not message or not message.strip():
        raise PredictionError("Message cannot be empty.")

    known = ml_model.get_known_symptoms()
    nlp_result = extract_symptoms(message.strip(), known)
    normalized = nlp_result["normalized"]

    if not normalized:
        raise PredictionError(
            "Could not identify any known symptoms from your message. "
            "Please try describing your symptoms more specifically, "
            "or use the symptom selection feature."
        )

    return _run_prediction(
        normalized_symptoms=normalized,
        input_mode="text",
        original_input=message,
        nlp_meta=nlp_result,
    )


def analyze_from_symptoms(symptom_list: list[str]) -> dict:
    """
    Process an icon-based symptom list and predict disease/specialist.

    Args:
        symptom_list: List of symptom name strings from frontend

    Returns:
        Full prediction response dict

    Raises:
        PredictionError: if no valid symptoms provided
    """
    if not symptom_list:
        raise PredictionError("Symptom list cannot be empty.")

    known = ml_model.get_known_symptoms()
    norm_result = normalize_icon_symptoms(symptom_list, known)
    normalized = norm_result["normalized"]
    unknown = norm_result["unknown"]

    if not normalized:
        raise PredictionError(
            f"None of the provided symptoms are recognized: {symptom_list}. "
            f"Use GET /api/symptoms to see the full list of valid symptoms."
        )

    return _run_prediction(
        normalized_symptoms=normalized,
        input_mode="icon",
        original_input=str(symptom_list),
        unknown_symptoms=unknown,
    )


def _run_prediction(
    normalized_symptoms: list[str],
    input_mode: str,
    original_input: str,
    nlp_meta: Optional[dict] = None,
    unknown_symptoms: Optional[list] = None,
) -> dict:
    """
    Core prediction runner. Calls ML model and builds the response.
    """
    # Limit to MAX_SYMPTOMS
    capped = normalized_symptoms[: config.MAX_SYMPTOMS]

    # Build symptom metadata list for the response
    symptom_details = []
    for name in capped:
        weight = ml_model.get_symptom_weight(name)
        if weight is not None:
            symptom_details.append(build_symptom_metadata(name, weight))

    # Run ML prediction
    result = ml_model.predict(capped)

    response = {
        "inputMode": input_mode,
        "normalizedSymptoms": capped,
        "symptomDetails": symptom_details,
        "predictedDisease": result["disease"],
        "recommendedSpecialist": result["specialist"],
        "confidence": result["confidence"],
        "diseaseDescription": result["description"],
        "precautions": result["precautions"],
        "severityScore": result["severity_score"],
        "severityLevel": result["severity_level"],
    }

    # Append NLP debug info for text mode
    if nlp_meta:
        response["nlpInfo"] = {
            "matchedPhrases": nlp_meta.get("matched_phrases", []),
            "fuzzyMatched": nlp_meta.get("fuzzy_matched", []),
            "unrecognizedTokens": nlp_meta.get("unrecognized_tokens", []),
        }

    # Append unknown symptoms warning
    if unknown_symptoms:
        response["warnings"] = [
            f"These symptoms were not recognized and were ignored: {unknown_symptoms}"
        ]

    logger.info(
        f"Prediction: [{input_mode}] '{original_input[:60]}' "
        f"-> {result['disease']} ({result['specialist']}) "
        f"confidence={result['confidence']:.2f}"
    )

    return response
