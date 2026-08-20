"""Routes package — registers all Blueprints."""

from .prediction_routes import prediction_bp
from .symptom_routes import symptom_bp
from .doctor_routes import doctor_bp

__all__ = ["prediction_bp", "symptom_bp", "doctor_bp"]
