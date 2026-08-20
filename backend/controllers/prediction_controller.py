"""
Prediction Controller — SymptoCare Backend

Handles POST /api/analyze-symptoms requests.
Accepts both natural language text and icon-based symptom list input.
"""

from __future__ import annotations
import logging
from flask import request

from services import prediction_service
from services.prediction_service import PredictionError
from utils.response import success_response, validation_error, server_error
from utils.validators import validate_symptoms_list

logger = logging.getLogger(__name__)


def analyze_symptoms():
    """
    POST /api/analyze-symptoms

    Accepts JSON body with either:
      { "message": "I have chest pain and trouble breathing" }
    OR:
      { "symptoms": ["chest_pain", "breathlessness"] }

    Returns a full prediction including disease, specialist, confidence,
    description, precautions, and severity.
    """
    body = request.get_json(silent=True)

    if not body:
        return validation_error(
            "Request body must be valid JSON with either a 'message' (string) "
            "or 'symptoms' (array of strings) field."
        )

    has_message = "message" in body
    has_symptoms = "symptoms" in body

    if not has_message and not has_symptoms:
        return validation_error(
            "Provide either 'message' (natural language) or 'symptoms' (array) in the request body."
        )

    try:
        if has_message:
            # Natural language path
            message = body["message"]
            if not isinstance(message, str) or not message.strip():
                return validation_error("'message' must be a non-empty string.")
            result = prediction_service.analyze_from_text(message.strip())

        else:
            # Icon-based path
            symptoms_raw = body["symptoms"]
            cleaned, err = validate_symptoms_list(symptoms_raw)
            if err:
                return validation_error(err)
            result = prediction_service.analyze_from_symptoms(cleaned)

    except PredictionError as e:
        return validation_error(str(e))
    except Exception as e:
        logger.exception(f"Unexpected error in analyze_symptoms: {e}")
        return server_error("Prediction failed. Please try again.")

    return success_response(result)
