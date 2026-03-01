from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import insert_user
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from datetime import timedelta
from db import SessionLocal  # SQLAlchemy session factory
from models.user_model import User

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    name = request.json.get("name")
    email = request.json.get("email")
    password = request.json.get("password")

    hashed_password = generate_password_hash(password)
    insert_user(name, email, hashed_password)

    return jsonify({"msg": "User Registered"})

@auth_bp.route("/login",methods=["POST"])
def login():
    email=request.json.get("email")
    password=request.json.get("password")
    session=SessionLocal()
    user=session.query(User).filter(User.email == email).first()
    session.close()
   
    if user and check_password_hash(user.password,password):
        access_token = create_access_token(
            identity=user.id,
         additional_claims={"role": "admin"},
         expires_delta=timedelta(minutes=15)

        )
        refresh_token=create_refresh_token(
            identity=user.id,
            expires_delta=timedelta(days=7)
        )
        return jsonify({
            "msg":"Login successfully",
            "access_token":access_token,
            "refresh_token":refresh_token
        })
    return jsonify({
        "msg":"invalid credentials"
    },401)       

@auth_bp.route("/profile",methods=["GET"])
@jwt_required()
def profile():
    user_id=get_jwt_identity()
    session=SessionLocal()
    user=session.query(User).filter(User.id== user_id).first()
    session.close()
    if not user:
        return jsonify({
            "msg":"User not Found"
        }),404
    return jsonify({
        "id":user.id,
        "name":user.name,
        "email":user
    })
    
    return jsonify({"msg":"Invalid credentials"}),401

@auth_bp.route("/admin",methods=["GET"])
@jwt_required()
def admin():
    claims=get_jwt()
    if claims.get("role")!="admin":
        return({
            "msg":"Admins only !"
        }),403
    return jsonify({
        "msg":"welcome admin"
    })