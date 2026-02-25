from flask import Blueprint, render_template, request, redirect, url_for
from models.user_model import get_all_users, insert_user, delete_user

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/")
def home():
    users = get_all_users()
    return render_template("users.html", users=users)


@user_bp.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        insert_user(name, email)
        return redirect(url_for("user_bp.home"))
    return render_template("add_user.html")


@user_bp.route("/delete/<int:user_id>")
def delete(user_id):
    delete_user(user_id)
    return redirect(url_for("user_bp.home"))