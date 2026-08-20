"""
Doctor Service — SymptoCare Backend

Handles searching for doctors and hospitals by:
  - Specialist category (mapped from ML prediction output)
  - Location (lat/lng with Haversine distance calculation)
  - City name (fallback when no lat/lng provided)

Data is loaded from JSON files at module init time (in-memory lookup).
Designed to be easily replaced with a real database query layer.
"""

from __future__ import annotations
import json
import logging
from typing import Optional

from config import config
from utils.distance import haversine_km

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# In-memory data store (loaded once at startup)
# ---------------------------------------------------------------------------
_doctors: list[dict] = []
_hospitals: list[dict] = []


def _load_data() -> None:
    """Load doctors and hospitals from JSON files into memory."""
    global _doctors, _hospitals

    try:
        with open(config.DOCTORS_DB_PATH, "r", encoding="utf-8") as f:
            _doctors = json.load(f)
        logger.info(f"Doctor Service: Loaded {len(_doctors)} doctors.")
    except FileNotFoundError:
        logger.error(f"Doctor Service: doctors.json not found at {config.DOCTORS_DB_PATH}")
        _doctors = []

    try:
        with open(config.HOSPITALS_DB_PATH, "r", encoding="utf-8") as f:
            _hospitals = json.load(f)
        logger.info(f"Doctor Service: Loaded {len(_hospitals)} hospitals.")
    except FileNotFoundError:
        logger.error(f"Doctor Service: hospitals.json not found at {config.HOSPITALS_DB_PATH}")
        _hospitals = []


def _add_distance(record: dict, user_lat: Optional[float], user_lng: Optional[float]) -> dict:
    """Add a formatted distance string to a doctor/hospital record."""
    result = dict(record)
    if user_lat is not None and user_lng is not None:
        dist_km = haversine_km(user_lat, user_lng, record["lat"], record["lng"])
        result["distance"] = f"{dist_km:.1f} km"
        result["_dist_km"] = dist_km  # used for sorting, removed later
    else:
        result["distance"] = None
        result["_dist_km"] = float("inf")
    return result


def _clean_record(record: dict) -> dict:
    """Remove internal sort keys before returning to client."""
    cleaned = dict(record)
    cleaned.pop("_dist_km", None)
    return cleaned


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def search_doctors(
    specialist: Optional[str] = None,
    lat: Optional[float] = None,
    lng: Optional[float] = None,
    city: Optional[str] = None,
    limit: int = config.MAX_RESULTS_DOCTORS,
    offset: int = 0,
) -> list[dict]:
    """
    Search doctors by specialist and/or location.

    Args:
        specialist:  Specialist category string (case-insensitive)
        lat, lng:    User's location for distance calculation and radius filter
        city:        City name filter (case-insensitive, used if no lat/lng)
        limit:       Maximum number of results to return

    Returns:
        List of doctor dicts sorted by distance (if lat/lng given) or rating
    """
    results = list(_doctors)

    # Filter by specialist (case-insensitive partial match)
    if specialist:
        spec_lower = specialist.strip().lower()
        results = [
            d for d in results
            if spec_lower in d["specialist"].lower()
        ]

    # Apply city filter:
    #   - If caller provides a city param, use that
    #   - If no lat/lng AND no city, fall back to DEFAULT_CITY (Chennai)
    effective_city = city
    if lat is None and effective_city is None:
        effective_city = config.DEFAULT_CITY

    if effective_city and lat is None:
        city_lower = effective_city.strip().lower()
        results = [d for d in results if d["city"].lower() == city_lower]

    # Add distance and sort
    results = [_add_distance(d, lat, lng) for d in results]

    # If lat/lng given, filter to radius + sort by distance
    if lat is not None and lng is not None:
        radius = config.DEFAULT_SEARCH_RADIUS_KM
        results = [d for d in results if d["_dist_km"] <= radius]
        results.sort(key=lambda x: x["_dist_km"])
    else:
        # Sort by rating descending
        results.sort(key=lambda x: x.get("rating", 0), reverse=True)

    # Apply limit and clean internal fields
    return [_clean_record(d) for d in results[offset:offset+limit]]


def search_hospitals(
    lat: Optional[float] = None,
    lng: Optional[float] = None,
    city: Optional[str] = None,
    specialist: Optional[str] = None,
    emergency_only: bool = False,
    limit: int = config.MAX_RESULTS_HOSPITALS,
) -> list[dict]:
    """
    Search hospitals by location and/or filters.

    Args:
        lat, lng:        User's location
        city:            City name filter
        specialist:      Filter hospitals that have this specialist
        emergency_only:  If True, only return hospitals with emergency services
        limit:           Maximum results

    Returns:
        List of hospital dicts sorted by distance or rating
    """
    results = list(_hospitals)

    if emergency_only:
        results = [h for h in results if h.get("emergency", False)]

    if specialist:
        spec_lower = specialist.strip().lower()
        results = [
            h for h in results
            if any(spec_lower in s.lower() for s in h.get("specialists", []))
        ]

    # Apply city filter with DEFAULT_CITY fallback
    effective_city = city
    if lat is None and effective_city is None:
        effective_city = config.DEFAULT_CITY

    if effective_city and lat is None:
        city_lower = effective_city.strip().lower()
        results = [h for h in results if h["city"].lower() == city_lower]

    results = [_add_distance(h, lat, lng) for h in results]

    if lat is not None and lng is not None:
        radius = config.DEFAULT_SEARCH_RADIUS_KM
        results = [h for h in results if h["_dist_km"] <= radius]
        results.sort(key=lambda x: x["_dist_km"])
    else:
        results.sort(key=lambda x: x.get("rating", 0), reverse=True)

    return [_clean_record(h) for h in results[:limit]]


def get_doctor_by_id(doctor_id: str) -> Optional[dict]:
    """Fetch a single doctor by ID."""
    for doc in _doctors:
        if doc["id"] == doctor_id:
            return dict(doc)
    return None


def get_hospital_by_id(hospital_id: str) -> Optional[dict]:
    """Fetch a single hospital by ID."""
    for hosp in _hospitals:
        if hosp["id"] == hospital_id:
            return dict(hosp)
    return None


def get_all_specialists() -> list[str]:
    """Return sorted list of unique specialist categories in the database."""
    specialists = sorted(set(d["specialist"] for d in _doctors))
    return specialists


# ---------------------------------------------------------------------------
# Load on module init
# ---------------------------------------------------------------------------
_load_data()
