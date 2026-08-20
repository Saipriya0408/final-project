"""
SymptoCare Backend API — Flask Application Entry Point

Startup sequence:
  1. Flask app created
  2. CORS configured
  3. ML model trained (one-time, ~2-5s)
  4. Doctor/hospital data loaded into memory
  5. All Blueprints registered
  6. Server starts

Run:
  python app.py
  
  Or with production server:
  gunicorn -w 2 -b 0.0.0.0:5000 app:app
"""

import logging
import os
import sys
from flask import Flask, jsonify
from flask_cors import CORS

# ---------------------------------------------------------------------------
# Logging setup (before any imports that log during module load)
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("symptocare")

# ---------------------------------------------------------------------------
# Ensure backend/ is in sys.path for absolute imports
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from config import config

# ---------------------------------------------------------------------------
# Create Flask app
# ---------------------------------------------------------------------------
app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False  # preserve dict insertion order in responses

# ---------------------------------------------------------------------------
# CORS — allow mobile app to call this API
# ---------------------------------------------------------------------------
CORS(
    app,
    origins=config.ALLOWED_ORIGINS,
    methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

# ---------------------------------------------------------------------------
# Register Blueprints
# ---------------------------------------------------------------------------
from routes import prediction_bp, symptom_bp, doctor_bp, auth_routes

app.register_blueprint(prediction_bp)
app.register_blueprint(symptom_bp)
app.register_blueprint(doctor_bp)
app.register_blueprint(auth_routes.auth_bp)

# ---------------------------------------------------------------------------
# Health check endpoint
# ---------------------------------------------------------------------------
@app.get("/api/health")
def health_check():
    """
    GET /api/health
    Returns server status and model readiness.
    Used by Android app and monitoring systems to verify backend is up.
    """
    from ml import model as ml_model
    model_ready = ml_model._rf_model is not None
    symptom_count = len(ml_model.get_known_symptoms())

    return jsonify({
        "success": True,
        "data": {
            "status": "ok",
            "service": "SymptoCare Backend API",
            "version": "1.0.0",
            "modelReady": model_ready,
            "knownSymptoms": symptom_count,
            "endpoints": [
                "POST /api/analyze-symptoms",
                "GET  /api/symptoms",
                "GET  /api/diseases",
                "GET  /api/doctors",
                "GET  /api/doctors/<id>",
                "GET  /api/hospitals",
                "GET  /api/hospitals/<id>",
                "GET  /api/specialists",
                "GET  /api/health",
            ],
        },
    }), 200


# ---------------------------------------------------------------------------
# Global error handlers
# ---------------------------------------------------------------------------
@app.errorhandler(404)
def not_found(e):
    return jsonify({
        "success": False,
        "error": {"code": "NOT_FOUND", "message": "Endpoint not found."},
    }), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        "success": False,
        "error": {"code": "METHOD_NOT_ALLOWED", "message": "HTTP method not allowed for this endpoint."},
    }), 405


@app.errorhandler(500)
def internal_error(e):
    logger.exception(f"Unhandled 500 error: {e}")
    return jsonify({
        "success": False,
        "error": {"code": "INTERNAL_ERROR", "message": "Internal server error."},
    }), 500


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    logger.info("=" * 60)
    logger.info("  SymptoCare Backend API")
    logger.info(f"  Host: {config.HOST}:{config.PORT}")
    logger.info(f"  Debug: {config.DEBUG}")
    logger.info(f"  Data directory: {config.DATA_DIR}")
    logger.info("=" * 60)

    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG,
    )
