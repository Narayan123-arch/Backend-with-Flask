from flask import Blueprint, render_template, request, redirect, url_for,jsonify
from models.user_model import get_all_users, insert_user, delete_user

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/")
def home():
    users = get_all_users()
    return render_template("users.html", users=users)


@user_bp.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        if request.is_json:
            data = request.get_json()
            name = data.get("name")
            email = data.get("email")
            password = data.get("password")  # optional

            # Make sure name and email are provided
            if not name or not email:
                return jsonify({"error": "Name and email are required"}), 400

            # Insert user
            insert_user(name, email, password)

            # Return success
            return jsonify({"message": "User added successfully"}), 201


@user_bp.route("/delete/<int:user_id>")
def delete(user_id):
    delete_user(user_id)
    return redirect(url_for("user_bp.home"))