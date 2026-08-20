from flask import Blueprint, request, jsonify
from services.auth_service import register_user, authenticate_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/auth/signup", methods=["POST"])
def signup():
    data = request.json
    if not data:
        return jsonify({"success": False, "error": {"message": "Invalid request"}}), 400
        
    name = data.get("name")
    phone = data.get("phone")
    email = data.get("email")
    password = data.get("password")
    
    if not all([name, phone, email, password]):
        return jsonify({"success": False, "error": {"message": "Missing required fields"}}), 400
        
    user, error = register_user(name, phone, email, password)
    
    if error:
        return jsonify({"success": False, "error": {"message": error}}), 409
        
    return jsonify({
        "success": True,
        "data": {
            "user": user,
            "token": f"mock_token_{user['id']}"  # Mock JWT token for MVP
        }
    }), 201

@auth_bp.route("/api/auth/login", methods=["POST"])
def login():
    data = request.json
    if not data:
        return jsonify({"success": False, "error": {"message": "Invalid request"}}), 400
        
    email_or_phone = data.get("email_or_phone")
    password = data.get("password")
    
    if not all([email_or_phone, password]):
        return jsonify({"success": False, "error": {"message": "Missing required fields"}}), 400
        
    user, error = authenticate_user(email_or_phone, password)
    
    if error:
        return jsonify({"success": False, "error": {"message": error}}), 401
        
    return jsonify({
        "success": True,
        "data": {
            "user": user,
            "token": f"mock_token_{user['id']}"
        }
    }), 200
