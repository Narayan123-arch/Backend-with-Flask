from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import insert_user
from db import get_connection

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
    conn=get_connection()
    cur=conn.cursor()
    cur.execute("SELECT password FROM nuser WHERE email=%s",(email,))
    user=cur.fetchone()
    cur.close()
    conn.close()
    if user and check_password_hash(user[0],password):
        access_token = create_access_token(identity=email, additional_claims={"role": "admin"})
        return jsonify({
            "msg":"Login successfully",
            "token":access_token
        })
    
    return jsonify({"msg":"Invalid credentials"}),401