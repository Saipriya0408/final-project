"""
Doctor routes Blueprint.

GET /api/doctors                - search doctors
GET /api/doctors/<id>           - get single doctor
GET /api/hospitals              - search hospitals
GET /api/hospitals/<id>         - get single hospital
GET /api/specialists            - list specialist categories
"""

from flask import Blueprint
from controllers.doctor_controller import (
    search_doctors,
    get_doctor,
    search_hospitals,
    get_hospital,
    get_specialists,
)

doctor_bp = Blueprint("doctors", __name__, url_prefix="/api")

doctor_bp.add_url_rule("/doctors", "search_doctors", search_doctors, methods=["GET"])
doctor_bp.add_url_rule("/doctors/<doctor_id>", "get_doctor", get_doctor, methods=["GET"])
doctor_bp.add_url_rule("/hospitals", "search_hospitals", search_hospitals, methods=["GET"])
doctor_bp.add_url_rule("/hospitals/<hospital_id>", "get_hospital", get_hospital, methods=["GET"])
doctor_bp.add_url_rule("/specialists", "get_specialists", get_specialists, methods=["GET"])
