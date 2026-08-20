"""
Standardized JSON response helpers for SymptoCare API.

All API endpoints use these helpers to ensure consistent response format:

Success:
  { "success": true, "data": {...} }

Error:
  { "success": false, "error": { "code": "...", "message": "..." } }
"""

from flask import jsonify


def success_response(data: dict | list, status_code: int = 200):
    """Wrap data in a standard success response."""
    return jsonify({"success": True, "data": data}), status_code


def error_response(message: str, code: str = "ERROR", status_code: int = 400):
    """Wrap an error in a standard error response."""
    return (
        jsonify({
            "success": False,
            "error": {
                "code": code,
                "message": message,
            },
        }),
        status_code,
    )


def validation_error(message: str):
    """Shorthand for 400 validation errors."""
    return error_response(message, code="VALIDATION_ERROR", status_code=400)


def not_found_error(message: str = "Resource not found."):
    """Shorthand for 404 errors."""
    return error_response(message, code="NOT_FOUND", status_code=404)


def server_error(message: str = "An internal server error occurred."):
    """Shorthand for 500 errors."""
    return error_response(message, code="INTERNAL_ERROR", status_code=500)
