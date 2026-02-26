from flask import Blueprint, render_template, request, redirect, url_for,jsonify
from models.user_model import get_all_users, insert_user, delete_user

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/")
def home():
    users = get_all_users()
    return render_template("users.html", users=users)


@user_bp.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json()

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email:
            return jsonify({"error": "Name and email required"}), 400

        insert_user(name, email, password)

        return jsonify({"message": "User added"}), 201

    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

@user_bp.route("/delete/<int:user_id>")
def delete(user_id):
    delete_user(user_id)
    return redirect(url_for("user_bp.home"))