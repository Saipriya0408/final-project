"""
Symptom Encoder — SymptoCare Backend

Handles the mapping between raw/informal symptom strings and the
canonical symptom names expected by the ML model (snake_case format).

Provides:
  - validate_symptoms(names)  → validated canonical names
  - symptom_info(name)        → name, display label, severity, category
  - all_symptoms_with_meta()  → full symptom list for the /api/symptoms endpoint
"""

from __future__ import annotations
import logging

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Symptom → UI category mapping
# Groups symptoms into logical categories for the mobile frontend icon picker.
# ---------------------------------------------------------------------------
SYMPTOM_CATEGORIES: dict[str, str] = {
    # Neurological
    "headache": "neurological",
    "dizziness": "neurological",
    "loss_of_balance": "neurological",
    "unsteadiness": "neurological",
    "altered_sensorium": "neurological",
    "lack_of_concentration": "neurological",
    "weakness_of_one_body_side": "neurological",
    "spinning_movements": "neurological",
    "visual_disturbances": "neurological",
    "blurred_and_distorted_vision": "neurological",
    "slurred_speech": "neurological",
    "coma": "neurological",
    "paralysis_(brain_hemorrhage)": "neurological",

    # Cardiac / Respiratory
    "chest_pain": "cardiac",
    "fast_heart_rate": "cardiac",
    "palpitations": "cardiac",
    "breathlessness": "respiratory",
    "cough": "respiratory",
    "phlegm": "respiratory",
    "mucoid_sputum": "respiratory",
    "rusty_sputum": "respiratory",
    "blood_in_sputum": "respiratory",
    "congestion": "respiratory",
    "runny_nose": "respiratory",
    "continuous_sneezing": "respiratory",
    "sinus_pressure": "respiratory",
    "throat_irritation": "respiratory",

    # Fever / Infection
    "fever": "fever",
    "high_fever": "fever",
    "mild_fever": "fever",
    "chills": "fever",
    "shivering": "fever",
    "sweating": "fever",
    "malaise": "fever",
    "toxic_look_(typhos)": "fever",

    # Gastrointestinal
    "nausea": "gastrointestinal",
    "vomiting": "gastrointestinal",
    "stomach_pain": "gastrointestinal",
    "abdominal_pain": "gastrointestinal",
    "belly_pain": "gastrointestinal",
    "indigestion": "gastrointestinal",
    "diarrhoea": "gastrointestinal",
    "constipation": "gastrointestinal",
    "acidity": "gastrointestinal",
    "passage_of_gases": "gastrointestinal",
    "stomach_bleeding": "gastrointestinal",
    "distention_of_abdomen": "gastrointestinal",
    "loss_of_appetite": "gastrointestinal",

    # Skin
    "itching": "skin",
    "skin_rash": "skin",
    "nodal_skin_eruptions": "skin",
    "dischromic_patches": "skin",
    "pus_filled_pimples": "skin",
    "blackheads": "skin",
    "scurring": "skin",
    "skin_peeling": "skin",
    "silver_like_dusting": "skin",
    "small_dents_in_nails": "skin",
    "inflammatory_nails": "skin",
    "blister": "skin",
    "red_sore_around_nose": "skin",
    "yellow_crust_ooze": "skin",
    "red_spots_over_body": "skin",

    # Musculoskeletal
    "joint_pain": "musculoskeletal",
    "knee_pain": "musculoskeletal",
    "hip_joint_pain": "musculoskeletal",
    "back_pain": "musculoskeletal",
    "neck_pain": "musculoskeletal",
    "muscle_wasting": "musculoskeletal",
    "muscle_weakness": "musculoskeletal",
    "muscle_pain": "musculoskeletal",
    "cramps": "musculoskeletal",
    "stiff_neck": "musculoskeletal",
    "swelling_joints": "musculoskeletal",
    "movement_stiffness": "musculoskeletal",
    "painful_walking": "musculoskeletal",

    # Eyes / ENT
    "redness_of_eyes": "eyes_ent",
    "pain_behind_the_eyes": "eyes_ent",
    "watering_from_eyes": "eyes_ent",
    "sunken_eyes": "eyes_ent",
    "puffy_face_and_eyes": "eyes_ent",
    "yellowing_of_eyes": "eyes_ent",
    "loss_of_smell": "eyes_ent",
    "patches_in_throat": "eyes_ent",
    "ulcers_on_tongue": "eyes_ent",

    # Urinary
    "burning_micturition": "urinary",
    "spotting_urination": "urinary",
    "foul_smell_ofurine": "urinary",
    "continuous_feel_of_urine": "urinary",
    "bladder_discomfort": "urinary",
    "yellow_urine": "urinary",
    "dark_urine": "urinary",

    # Metabolic / Hormonal
    "weight_gain": "metabolic",
    "weight_loss": "metabolic",
    "obesity": "metabolic",
    "excessive_hunger": "metabolic",
    "increased_appetite": "metabolic",
    "irregular_sugar_level": "metabolic",
    "polyuria": "metabolic",
    "enlarged_thyroid": "metabolic",
    "cold_hands_and_feets": "metabolic",
    "drying_and_tingling_lips": "metabolic",

    # General / Systemic
    "fatigue": "general",
    "lethargy": "general",
    "restlessness": "general",
    "anxiety": "general",
    "mood_swings": "general",
    "depression": "general",
    "irritability": "general",
    "dehydration": "general",
    "weakness_in_limbs": "general",
    "swelled_lymph_nodes": "general",
    "brittle_nails": "general",
    "swollen_extremeties": "general",
    "swollen_legs": "general",
    "swollen_blood_vessels": "general",
    "prominent_veins_on_calf": "general",

    # Liver / Blood
    "yellowish_skin": "liver",
    "acute_liver_failure": "liver",
    "fluid_overload": "liver",
    "swelling_of_stomach": "liver",

    # Other / Reproductive
    "abnormal_menstruation": "reproductive",
    "internal_itching": "reproductive",

    # Infection markers
    "receiving_blood_transfusion": "infection_markers",
    "receiving_unsterile_injections": "infection_markers",
    "extra_marital_contacts": "infection_markers",
    "family_history": "infection_markers",
    "history_of_alcohol_consumption": "infection_markers",

    # Bowel / Rectal
    "pain_during_bowel_movements": "bowel",
    "pain_in_anal_region": "bowel",
    "bloody_stool": "bowel",
    "irritation_in_anus": "bowel",

    # Liver/Jaundice
    "prognosis": "liver",
}

# Display labels: snake_case → Human-readable string
_DISPLAY_LABELS: dict[str, str] = {}


def _build_display_label(name: str) -> str:
    """Convert snake_case symptom name to Title Case display label."""
    return name.replace("_", " ").replace("(", "").replace(")", "").title()


def get_symptom_category(symptom_name: str) -> str:
    return SYMPTOM_CATEGORIES.get(symptom_name.strip(), "general")


def get_display_label(symptom_name: str) -> str:
    if symptom_name not in _DISPLAY_LABELS:
        _DISPLAY_LABELS[symptom_name] = _build_display_label(symptom_name)
    return _DISPLAY_LABELS[symptom_name]


def validate_symptoms(names: list[str], known_symptoms: list[str]) -> tuple[list[str], list[str]]:
    """
    Validate a list of symptom names against the model's known symptoms.

    Returns:
        (valid_symptoms, unknown_symptoms)
    """
    known_set = set(known_symptoms)
    valid = []
    unknown = []
    for name in names:
        clean = name.strip().lower().replace(" ", "_")
        if clean in known_set:
            valid.append(clean)
        else:
            unknown.append(name)
    return valid, unknown


def build_symptom_metadata(symptom_name: str, weight: float) -> dict:
    """Build the full metadata dict for a single symptom."""
    return {
        "name": symptom_name,
        "display": get_display_label(symptom_name),
        "severity": int(weight),
        "category": get_symptom_category(symptom_name),
    }
