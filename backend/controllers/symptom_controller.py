"""
Symptom Controller — SymptoCare Backend

Handles GET /api/symptoms requests.
Returns the full list of 134 symptoms with metadata for the frontend icon picker.
"""

from __future__ import annotations
import logging

from ml import model as ml_model
from ml.symptom_encoder import build_symptom_metadata
from utils.response import success_response, server_error

logger = logging.getLogger(__name__)


def get_symptoms():
    """
    GET /api/symptoms

    Returns all known symptoms with display names, severity levels, and
    category tags for building the mobile icon-selection UI.

    Optional query param: ?category=cardiac  (filter by category)
    """
    from flask import request

    category_filter = request.args.get("category", "").strip().lower()

    try:
        known = ml_model.get_known_symptoms()
        symptoms_meta = []

        for name in known:
            weight = ml_model.get_symptom_weight(name)
            meta = build_symptom_metadata(name, weight or 0)
            if category_filter and meta["category"] != category_filter:
                continue
            symptoms_meta.append(meta)

        # Sort by category then display name for consistent UI ordering
        symptoms_meta.sort(key=lambda x: (x["category"], x["display"]))

        return success_response({
            "total": len(symptoms_meta),
            "filtered": bool(category_filter),
            "categoryFilter": category_filter or None,
            "symptoms": symptoms_meta,
        })

    except Exception as e:
        logger.exception(f"Error in get_symptoms: {e}")
        return server_error("Failed to retrieve symptom list.")


def get_diseases():
    """
    GET /api/diseases

    Returns all 41 diseases with descriptions and specialist mappings.
    Useful for educational/informational screens in the app.
    """
    try:
        from ml import model as ml_model
        diseases = []
        # Collect from disease->specialist map
        for disease, specialist in ml_model._disease_specialist_map.items():
            diseases.append({
                "name": disease,
                "specialist": specialist,
                "description": ml_model.get_disease_description(disease),
                "precautions": ml_model.get_disease_precautions(disease),
            })
        diseases.sort(key=lambda x: x["name"])
        return success_response({"total": len(diseases), "diseases": diseases})
    except Exception as e:
        logger.exception(f"Error in get_diseases: {e}")
        return server_error("Failed to retrieve disease list.")
