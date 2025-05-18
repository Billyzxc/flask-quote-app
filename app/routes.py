from flask import Blueprint, render_template, request, redirect, url_for, flash, session

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # 簡化：此處應查 DB 進行密碼驗證
        if username == "admin" and password == "password":
            session["user"] = username
            return redirect(url_for("main.dashboard"))
        flash("Invalid credentials")
    return render_template("login.html")

@main.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("main.login"))
    return render_template("dashboard.html")
