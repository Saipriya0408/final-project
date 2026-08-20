"""
Doctor Controller — SymptoCare Backend

Handles:
  GET /api/doctors           - search doctors by specialist + location
  GET /api/doctors/<id>      - get doctor details (for call/appointment)
  GET /api/hospitals         - search hospitals by location
  GET /api/hospitals/<id>    - get hospital details
  GET /api/specialists       - list all specialist categories
"""

from __future__ import annotations
import logging
from flask import request

from services import doctor_service
from utils.response import success_response, validation_error, not_found_error, server_error
from utils.validators import validate_lat_lng, parse_int
from config import config

logger = logging.getLogger(__name__)


def search_doctors():
    """
    GET /api/doctors

    Query params:
      specialist  - Specialist category (e.g., "cardiologist")
      lat         - User latitude
      lng         - User longitude
      city        - City name (used if no lat/lng provided)
      limit       - Max results (default 20)
    """
    specialist = request.args.get("specialist", "").strip() or None
    lat_str = request.args.get("lat")
    lng_str = request.args.get("lng")
    city = request.args.get("city", "").strip() or None
    limit_str = request.args.get("limit")
    offset_str = request.args.get("offset")

    lat, lng, err = validate_lat_lng(lat_str, lng_str)
    if err:
        return validation_error(err)

    limit, err = parse_int(limit_str, "limit", 1, 50)
    if err:
        return validation_error(err)
    if limit is None:
        limit = config.MAX_RESULTS_DOCTORS

    offset, err = parse_int(offset_str, "offset", 0, 10000)
    if err:
        return validation_error(err)
    if offset is None:
        offset = 0

    try:
        doctors = doctor_service.search_doctors(
            specialist=specialist,
            lat=lat,
            lng=lng,
            city=city,
            limit=limit,
            offset=offset,
        )
        return success_response({
            "total": len(doctors),
            "specialist": specialist,
            "locationBased": lat is not None,
            "doctors": doctors,
        })
    except Exception as e:
        logger.exception(f"Error in search_doctors: {e}")
        return server_error("Failed to retrieve doctors.")


def get_doctor(doctor_id: str):
    """
    GET /api/doctors/<doctor_id>

    Returns full doctor details including phone for call-to-book.
    """
    try:
        doctor = doctor_service.get_doctor_by_id(doctor_id)
        if not doctor:
            return not_found_error(f"Doctor with ID '{doctor_id}' not found.")
        return success_response(doctor)
    except Exception as e:
        logger.exception(f"Error in get_doctor({doctor_id}): {e}")
        return server_error("Failed to retrieve doctor details.")


def search_hospitals():
    """
    GET /api/hospitals

    Query params:
      lat            - User latitude
      lng            - User longitude
      city           - City name fallback
      specialist     - Filter hospitals that have this specialist
      emergency_only - If "true", only return emergency hospitals
      limit          - Max results (default 10)
    """
    lat_str = request.args.get("lat")
    lng_str = request.args.get("lng")
    city = request.args.get("city", "").strip() or None
    specialist = request.args.get("specialist", "").strip() or None
    emergency_only = request.args.get("emergency_only", "false").lower() == "true"
    limit_str = request.args.get("limit")

    lat, lng, err = validate_lat_lng(lat_str, lng_str)
    if err:
        return validation_error(err)

    limit, err = parse_int(limit_str, "limit", 1, 50)
    if err:
        return validation_error(err)
    if limit is None:
        limit = config.MAX_RESULTS_HOSPITALS

    try:
        hospitals = doctor_service.search_hospitals(
            lat=lat,
            lng=lng,
            city=city,
            specialist=specialist,
            emergency_only=emergency_only,
            limit=limit,
        )
        return success_response({
            "total": len(hospitals),
            "locationBased": lat is not None,
            "emergencyOnly": emergency_only,
            "hospitals": hospitals,
        })
    except Exception as e:
        logger.exception(f"Error in search_hospitals: {e}")
        return server_error("Failed to retrieve hospitals.")


def get_hospital(hospital_id: str):
    """
    GET /api/hospitals/<hospital_id>

    Returns full hospital details including phone and emergency number.
    """
    try:
        hospital = doctor_service.get_hospital_by_id(hospital_id)
        if not hospital:
            return not_found_error(f"Hospital with ID '{hospital_id}' not found.")
        return success_response(hospital)
    except Exception as e:
        logger.exception(f"Error in get_hospital({hospital_id}): {e}")
        return server_error("Failed to retrieve hospital details.")


def get_specialists():
    """
    GET /api/specialists

    Returns all specialist categories available in the doctor database.
    Useful for populating filter dropdowns in the frontend.
    """
    try:
        specialists = doctor_service.get_all_specialists()
        return success_response({"total": len(specialists), "specialists": specialists})
    except Exception as e:
        logger.exception(f"Error in get_specialists: {e}")
        return server_error("Failed to retrieve specialists.")
