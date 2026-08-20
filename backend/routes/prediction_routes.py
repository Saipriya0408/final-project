"""
Prediction routes Blueprint.

POST /api/analyze-symptoms
"""

from flask import Blueprint
from controllers.prediction_controller import analyze_symptoms

prediction_bp = Blueprint("prediction", __name__, url_prefix="/api")

prediction_bp.add_url_rule(
    "/analyze-symptoms",
    "analyze_symptoms",
    analyze_symptoms,
    methods=["POST"],
)
