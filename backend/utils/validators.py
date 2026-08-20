"""
Input validation helpers for SymptoCare API.

Used by controllers to validate and sanitize request parameters
before passing them to the service layer.
"""

from __future__ import annotations
from typing import Optional


def parse_float(value: str, name: str) -> tuple[Optional[float], Optional[str]]:
    """
    Parse a string to float. Returns (value, None) on success or (None, error_msg).
    """
    if value is None:
        return None, None
    try:
        return float(value), None
    except (ValueError, TypeError):
        return None, f"Parameter '{name}' must be a valid number. Got: '{value}'"


def parse_int(value: str, name: str, min_val: int = 1, max_val: int = 100) -> tuple[Optional[int], Optional[str]]:
    """
    Parse a string to int within [min_val, max_val]. Returns (value, None) or (None, error_msg).
    """
    if value is None:
        return None, None
    try:
        v = int(value)
        if v < min_val or v > max_val:
            return None, f"Parameter '{name}' must be between {min_val} and {max_val}. Got: {v}"
        return v, None
    except (ValueError, TypeError):
        return None, f"Parameter '{name}' must be a valid integer. Got: '{value}'"


def validate_lat_lng(lat_str: Optional[str], lng_str: Optional[str]) -> tuple[Optional[float], Optional[float], Optional[str]]:
    """
    Validate and parse latitude/longitude query params.

    Returns:
        (lat, lng, error_message)
        lat/lng are None if not provided.
        error_message is None if valid.
    """
    lat, err = parse_float(lat_str, "lat")
    if err:
        return None, None, err

    lng, err = parse_float(lng_str, "lng")
    if err:
        return None, None, err

    if lat is not None and not (-90 <= lat <= 90):
        return None, None, f"Latitude must be between -90 and 90. Got: {lat}"

    if lng is not None and not (-180 <= lng <= 180):
        return None, None, f"Longitude must be between -180 and 180. Got: {lng}"

    # lat and lng must be provided together
    if (lat is None) != (lng is None):
        return None, None, "Both 'lat' and 'lng' must be provided together."

    return lat, lng, None


def validate_symptoms_list(symptoms: list) -> tuple[list[str], Optional[str]]:
    """
    Validate that symptoms is a non-empty list of strings.
    """
    if not isinstance(symptoms, list):
        return [], "Field 'symptoms' must be a JSON array of strings."
    if len(symptoms) == 0:
        return [], "Field 'symptoms' cannot be empty."
    if not all(isinstance(s, str) for s in symptoms):
        return [], "All items in 'symptoms' must be strings."
    cleaned = [s.strip() for s in symptoms if s.strip()]
    if not cleaned:
        return [], "Field 'symptoms' contains only empty strings."
    return cleaned, None
