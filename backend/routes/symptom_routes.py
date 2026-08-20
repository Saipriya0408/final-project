"""
Symptom routes Blueprint.

GET /api/symptoms
GET /api/diseases
"""

from flask import Blueprint
from controllers.symptom_controller import get_symptoms, get_diseases

symptom_bp = Blueprint("symptoms", __name__, url_prefix="/api")

symptom_bp.add_url_rule("/symptoms", "get_symptoms", get_symptoms, methods=["GET"])
symptom_bp.add_url_rule("/diseases", "get_diseases", get_diseases, methods=["GET"])
