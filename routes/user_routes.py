from flask import Blueprint, render_template, request, redirect, url_for,jsonify
from models.user_model import get_all_users, insert_user, delete_user,update_user

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

@user_bp.route("/update/<int:user_id>",methods=["PUT"])
def update_user_route(user_id):
    data=request.get_json()

    updated_user=update_user(
        user_id,
        name=data.get("name"),
        email=data.get("email"),
        password=data.get("password")

    )
    if not updated_user:
        return jsonify({"message":"user not found"}),401
    return jsonify({"message":"user updated successfully"})