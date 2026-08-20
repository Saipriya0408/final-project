"""
NLP Service — SymptoCare Backend

Converts informal natural language symptom descriptions into normalized
symptom names compatible with the ML model.

Pipeline:
  1. Preprocess text (lowercase, strip stopwords, punctuation)
  2. Multi-word phrase matching against a synonym dictionary
  3. Single-word fuzzy matching against known symptoms
  4. Validate results against the model's known symptom list

Approach: Lightweight — uses only Python stdlib (difflib) + a hand-crafted
synonym dictionary. No LLMs, no heavy NLP frameworks required.

Examples:
  "my head hurts and I feel feverish" -> ["headache", "fever"]
  "bro chest tight can't breathe"     -> ["chest_pain", "breathlessness"]
  "having loose motions since 2 days" -> ["diarrhoea"]
"""

from __future__ import annotations
import re
import logging
from difflib import get_close_matches

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Stopwords to strip from user input before matching
# ---------------------------------------------------------------------------
_STOPWORDS = {
    "i", "me", "my", "myself", "we", "our", "have", "has", "am", "is", "are",
    "was", "were", "be", "been", "being", "do", "does", "did", "doing", "a",
    "an", "the", "and", "but", "or", "nor", "so", "yet", "for", "at", "by",
    "in", "of", "on", "to", "up", "as", "if", "he", "him", "his", "she",
    "her", "it", "its", "they", "them", "their", "what", "which", "who",
    "this", "that", "these", "those", "some", "such", "not", "no", "very",
    "just", "too", "also", "with", "from", "had", "can", "will", "would",
    "could", "should", "may", "might", "shall", "must", "few", "more", "most",
    "other", "any", "each", "both", "all", "get", "got", "feel", "feeling",
    "felt", "since", "days", "day", "weeks", "week", "hours", "hour", "past",
    "ago", "now", "today", "yesterday", "morning", "night", "really", "bit",
    "little", "lot", "always", "often", "sometimes", "bro", "dude", "man",
    "like", "kinda", "sorta", "okay", "ok", "yeah", "yea", "hey", "hi",
    "hello", "please", "help", "think", "thought", "seems", "seemed", "seem",
    "experiencing", "experience", "having", "getting", "going", "going",
    "suffering", "suffer", "complain", "complaining",
}

# ---------------------------------------------------------------------------
# Synonym dictionary
# Maps informal/colloquial phrases -> canonical symptom names
# Longer phrases checked first (most-specific-first matching)
# ---------------------------------------------------------------------------
SYNONYM_MAP: dict[str, str] = {
    # ---- Headache ----
    "head hurts": "headache",
    "head is hurting": "headache",
    "head pain": "headache",
    "head ache": "headache",
    "headache": "headache",
    "migraines": "headache",
    "migraine": "headache",
    "head is pounding": "headache",
    "pounding head": "headache",
    "throbbing head": "headache",
    "my head": "headache",

    # ---- Fever ----
    "feverish": "high_fever",
    "running a fever": "high_fever",
    "running fever": "high_fever",
    "temperature": "high_fever",
    "high temperature": "high_fever",
    "high fever": "high_fever",
    "mild fever": "mild_fever",
    "low grade fever": "mild_fever",
    "slight fever": "mild_fever",
    "fever": "high_fever",
    "hot body": "high_fever",
    "body heat": "high_fever",

    # ---- Chest ----
    "chest pain": "chest_pain",
    "chest hurts": "chest_pain",
    "chest ache": "chest_pain",
    "tight chest": "chest_pain",
    "chest tightness": "chest_pain",
    "chest feels tight": "chest_pain",
    "pressure in chest": "chest_pain",
    "heaviness in chest": "chest_pain",
    "chest is heavy": "chest_pain",
    "heart pain": "chest_pain",

    # ---- Breathing ----
    "breathing issues": "breathlessness",
    "breathing problem": "breathlessness",
    "trouble breathing": "breathlessness",
    "difficulty breathing": "breathlessness",
    "hard to breathe": "breathlessness",
    "cant breathe": "breathlessness",
    "can't breathe": "breathlessness",
    "short of breath": "breathlessness",
    "shortness of breath": "breathlessness",
    "out of breath": "breathlessness",
    "breathless": "breathlessness",
    "breathlessness": "breathlessness",

    # ---- Cough ----
    "coughing": "cough",
    "cough": "cough",
    "dry cough": "cough",
    "wet cough": "cough",
    "constant cough": "cough",
    "persistent cough": "cough",
    "coughing up blood": "blood_in_sputum",
    "blood in cough": "blood_in_sputum",

    # ---- Vomiting / Nausea ----
    "throwing up": "vomiting",
    "threw up": "vomiting",
    "puking": "vomiting",
    "puke": "vomiting",
    "vomiting": "vomiting",
    "vomit": "vomiting",
    "feel like vomiting": "nausea",
    "want to vomit": "nausea",
    "nauseous": "nausea",
    "feel nauseous": "nausea",
    "nausea": "nausea",
    "queasy": "nausea",
    "stomach upset": "nausea",

    # ---- Stomach / Abdomen ----
    "stomach ache": "stomach_pain",
    "stomach pain": "stomach_pain",
    "stomach hurts": "stomach_pain",
    "tummy ache": "stomach_pain",
    "tummy pain": "stomach_pain",
    "belly pain": "belly_pain",
    "belly ache": "belly_pain",
    "abdominal pain": "abdominal_pain",
    "lower abdomen pain": "abdominal_pain",
    "cramps": "cramps",
    "stomach cramps": "cramps",

    # ---- Diarrhoea ----
    "loose stools": "diarrhoea",
    "loose motions": "diarrhoea",
    "loose stool": "diarrhoea",
    "watery stools": "diarrhoea",
    "runny stool": "diarrhoea",
    "diarrhea": "diarrhoea",
    "diarrhoea": "diarrhoea",
    "frequent stools": "diarrhoea",

    # ---- Skin ----
    "skin itching": "itching",
    "itchy skin": "itching",
    "itching": "itching",
    "itch": "itching",
    "rashes": "skin_rash",
    "rash": "skin_rash",
    "skin rash": "skin_rash",
    "red rash": "skin_rash",
    "pimples": "pus_filled_pimples",
    "acne": "pus_filled_pimples",
    "blackheads": "blackheads",
    "skin peeling": "skin_peeling",
    "peeling skin": "skin_peeling",

    # ---- Eyes ----
    "red eyes": "redness_of_eyes",
    "eyes red": "redness_of_eyes",
    "eye redness": "redness_of_eyes",
    "watery eyes": "watering_from_eyes",
    "eyes watering": "watering_from_eyes",
    "blurry vision": "blurred_and_distorted_vision",
    "blurred vision": "blurred_and_distorted_vision",
    "vision problem": "blurred_and_distorted_vision",
    "yellow eyes": "yellowing_of_eyes",
    "eyes are yellow": "yellowing_of_eyes",
    "pain behind eyes": "pain_behind_the_eyes",

    # ---- Fatigue / Weakness ----
    "tired": "fatigue",
    "tiredness": "fatigue",
    "exhausted": "fatigue",
    "exhaustion": "fatigue",
    "fatigue": "fatigue",
    "weak": "weakness_in_limbs",
    "weakness": "weakness_in_limbs",
    "body weakness": "weakness_in_limbs",
    "no energy": "fatigue",
    "low energy": "fatigue",
    "lethargic": "lethargy",
    "lethargy": "lethargy",
    "lazy": "lethargy",

    # ---- Joint / Muscle Pain ----
    "joint pain": "joint_pain",
    "joints hurt": "joint_pain",
    "joint ache": "joint_pain",
    "muscle pain": "muscle_pain",
    "muscle ache": "muscle_pain",
    "body ache": "muscle_pain",
    "body pain": "muscle_pain",
    "back pain": "back_pain",
    "back ache": "back_pain",
    "lower back pain": "back_pain",
    "neck pain": "neck_pain",
    "stiff neck": "stiff_neck",
    "knee pain": "knee_pain",
    "hip pain": "hip_joint_pain",

    # ---- Dizziness / Vertigo ----
    "dizzy": "dizziness",
    "dizziness": "dizziness",
    "lightheaded": "dizziness",
    "lightheadedness": "dizziness",
    "vertigo": "spinning_movements",
    "room spinning": "spinning_movements",
    "head spinning": "spinning_movements",

    # ---- Urinary ----
    "burning urination": "burning_micturition",
    "burning when urinating": "burning_micturition",
    "painful urination": "burning_micturition",
    "frequent urination": "continuous_feel_of_urine",
    "urge to urinate": "continuous_feel_of_urine",
    "dark urine": "dark_urine",
    "yellow urine": "yellow_urine",
    "blood in urine": "burning_micturition",

    # ---- Swelling ----
    "swollen legs": "swollen_legs",
    "legs swollen": "swollen_legs",
    "swollen feet": "swollen_legs",
    "puffy face": "puffy_face_and_eyes",
    "face swollen": "puffy_face_and_eyes",
    "swollen joints": "swelling_joints",

    # ---- Cold / Congestion ----
    "runny nose": "runny_nose",
    "stuffy nose": "congestion",
    "blocked nose": "congestion",
    "congestion": "congestion",
    "sneezing": "continuous_sneezing",
    "sneeze": "continuous_sneezing",
    "cold": "continuous_sneezing",
    "common cold": "continuous_sneezing",
    "sore throat": "throat_irritation",
    "throat pain": "throat_irritation",
    "throat irritation": "throat_irritation",

    # ---- Weight / Appetite ----
    "losing weight": "weight_loss",
    "weight loss": "weight_loss",
    "weight gain": "weight_gain",
    "gaining weight": "weight_gain",
    "no appetite": "loss_of_appetite",
    "not hungry": "loss_of_appetite",
    "loss of appetite": "loss_of_appetite",
    "very hungry": "excessive_hunger",
    "always hungry": "excessive_hunger",

    # ---- Mood / Mental ----
    "anxiety": "anxiety",
    "anxious": "anxiety",
    "panic": "anxiety",
    "depressed": "depression",
    "depression": "depression",
    "mood swings": "mood_swings",
    "irritable": "irritability",
    "irritability": "irritability",
    "restless": "restlessness",
    "restlessness": "restlessness",

    # ---- Jaundice / Liver ----
    "yellow skin": "yellowish_skin",
    "yellowish skin": "yellowish_skin",
    "jaundice": "yellowish_skin",
    "liver problem": "acute_liver_failure",

    # ---- Other ----
    "sweating": "sweating",
    "excessive sweating": "sweating",
    "night sweats": "sweating",
    "chills": "chills",
    "shivering": "shivering",
    "dehydration": "dehydration",
    "constipation": "constipation",
    "indigestion": "indigestion",
    "heartburn": "acidity",
    "acid reflux": "acidity",
    "gas": "passage_of_gases",
    "bloating": "passage_of_gases",
    "piles": "pain_in_anal_region",
    "hemorrhoids": "pain_in_anal_region",
}

# Sort by phrase length descending so longer phrases match first
_SORTED_PHRASES = sorted(SYNONYM_MAP.keys(), key=len, reverse=True)


def _preprocess_text(text: str) -> str:
    """
    Clean input text:
      - Lowercase
      - Remove special characters except spaces
      - Collapse multiple spaces
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)   # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _remove_stopwords(tokens: list[str]) -> list[str]:
    return [t for t in tokens if t not in _STOPWORDS and len(t) > 1]


def _phrase_match(text: str) -> tuple[list[str], str]:
    """
    Greedily match multi-word phrases from the synonym dictionary.
    Returns matched canonical names and the remaining unmatched text.
    """
    found = []
    remaining = text

    for phrase in _SORTED_PHRASES:
        if phrase in remaining:
            canonical = SYNONYM_MAP[phrase]
            if canonical not in found:
                found.append(canonical)
            # Remove the matched phrase to avoid double-counting
            remaining = remaining.replace(phrase, " ")
            remaining = re.sub(r"\s+", " ", remaining).strip()

    return found, remaining


def _fuzzy_match_tokens(tokens: list[str], known_symptoms: list[str]) -> list[str]:
    """
    For each unmatched token, try fuzzy-matching it against known symptom names.
    Uses difflib.get_close_matches with a cutoff of 0.75.
    """
    found = []
    for token in tokens:
        if len(token) < 4:
            continue
        matches = get_close_matches(token, known_symptoms, n=1, cutoff=0.75)
        if matches and matches[0] not in found:
            found.append(matches[0])
    return found


def extract_symptoms(text: str, known_symptoms: list[str]) -> dict:
    """
    Main entry point. Extracts and normalizes symptoms from free-form text.

    Args:
        text:            User's natural language input
        known_symptoms:  List of canonical symptom names from the ML model

    Returns:
        {
            "normalized": list[str],   # canonical symptom names
            "matched_phrases": list[str],
            "fuzzy_matched": list[str],
            "unrecognized_tokens": list[str],
        }
    """
    cleaned = _preprocess_text(text)
    logger.debug(f"NLP: cleaned text = '{cleaned}'")

    # Step 1: Multi-word phrase matching
    phrase_found, remaining_text = _phrase_match(cleaned)
    logger.debug(f"NLP: phrase matches = {phrase_found}, remaining = '{remaining_text}'")

    # Step 2: Tokenize remaining text and remove stopwords
    remaining_tokens = _remove_stopwords(remaining_text.split())
    logger.debug(f"NLP: remaining tokens after stopwords = {remaining_tokens}")

    # Step 3: Single-token synonym dict check
    token_found_dict = []
    still_unmatched = []
    for token in remaining_tokens:
        if token in SYNONYM_MAP:
            canonical = SYNONYM_MAP[token]
            if canonical not in phrase_found and canonical not in token_found_dict:
                token_found_dict.append(canonical)
        else:
            still_unmatched.append(token)

    # Step 4: Fuzzy match remaining tokens against known symptoms
    fuzzy_found = _fuzzy_match_tokens(still_unmatched, known_symptoms)

    # Track genuinely unrecognized tokens
    fuzzy_set = set(fuzzy_found)
    unrecognized = [t for t in still_unmatched if t not in fuzzy_set]

    # Combine all found symptoms, de-duplicate, preserve order
    all_found = []
    seen = set()
    for sym in phrase_found + token_found_dict + fuzzy_found:
        if sym not in seen:
            # Final validation: must be in known symptoms
            if sym in known_symptoms:
                all_found.append(sym)
                seen.add(sym)
            else:
                logger.debug(f"NLP: discarded '{sym}' — not in known symptoms")

    logger.info(f"NLP: '{text}' -> {all_found}")
    return {
        "normalized": all_found,
        "matched_phrases": phrase_found,
        "fuzzy_matched": fuzzy_found,
        "unrecognized_tokens": unrecognized,
    }


def normalize_icon_symptoms(symptom_list: list[str], known_symptoms: list[str]) -> dict:
    """
    Normalize icon-based symptom input (frontend sends clean names).
    Handles minor variations: spaces → underscores, case-insensitive lookup.

    Args:
        symptom_list:   List of symptom strings from frontend
        known_symptoms: Canonical symptom names from ML model

    Returns:
        {
            "normalized": list[str],
            "unknown": list[str],
        }
    """
    known_set = set(known_symptoms)
    normalized = []
    unknown = []

    # Map static layout icons to model canonical terms
    icon_mappings = {
        "eye_problem": "redness_of_eyes",
        "breathing_issue": "breathlessness",
        "ear_pain": "sinus_pressure",
        "skin_problem": "skin_rash"
    }

    for raw in symptom_list:
        clean_raw = raw.strip().lower()
        candidate = clean_raw.replace(" ", "_").replace("-", "_")

        # Intercept custom static icon overrides
        if candidate in icon_mappings:
            candidate = icon_mappings[candidate]
        elif clean_raw in icon_mappings:
            candidate = icon_mappings[clean_raw]

        if candidate in known_set:
            normalized.append(candidate)
        else:
            # Try synonym map (with and without spaces)
            mapped = (
                SYNONYM_MAP.get(candidate)
                or SYNONYM_MAP.get(clean_raw)
                or SYNONYM_MAP.get(candidate.replace("_", " "))
            )
            if mapped and mapped in known_set:
                normalized.append(mapped)
            else:
                # Fuzzy fallback
                matches = get_close_matches(candidate, known_symptoms, n=1, cutoff=0.80)
                if matches:
                    normalized.append(matches[0])
                else:
                    unknown.append(raw)

    # De-duplicate preserving order
    seen = set()
    deduped = []
    for s in normalized:
        if s not in seen:
            deduped.append(s)
            seen.add(s)

    return {"normalized": deduped, "unknown": unknown}
