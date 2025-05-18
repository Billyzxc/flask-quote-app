from flask import Blueprint, render_template, request, redirect, url_for, flash, session

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
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

@main.route("/access-panel")
def access_panel():
    if "user" not in session:
        return redirect(url_for("main.login"))
    return render_template("access-panel.html")

@main.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.")
    return redirect(url_for("main.login"))


