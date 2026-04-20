#!/usr/bin/python3
"""Flask API with Basic Auth and JWT security + role-based access control."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)
auth = HTTPBasicAuth()

# In-memory users
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# -----------------------
# BASIC AUTH
# -----------------------
@auth.verify_password
def verify(username, password):
    """Verify basic auth credentials."""
    if username in users:
        return check_password_hash(users[username]["password"], password)
    return False


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Basic auth protected route."""
    return "Basic Auth: Access Granted"


# -----------------------
# JWT LOGIN
# -----------------------
@app.route("/login", methods=["POST"])
def login():
    """Authenticate user and return JWT token."""
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=username)
    return jsonify({"access_token": token})


# -----------------------
# JWT PROTECTED ROUTE
# -----------------------
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """JWT protected route."""
    return "JWT Auth: Access Granted"


# -----------------------
# ADMIN ONLY ROUTE
# -----------------------
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Admin-only route using role-based access control."""
    username = get_jwt_identity()
    user = users.get(username)

    if user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# -----------------------
# JWT ERROR HANDLERS
# -----------------------
@jwt.unauthorized_loader
def missing_token_callback(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def fresh_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
