from flask import Blueprint, render_template, request, redirect, url_for, session

main = Blueprint("main", __name__)

# 初始帳密（模擬資料庫）
users = {"admin": "password"}

@main.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("main.dashboard"))
        error = "帳號或密碼錯誤"
    return render_template("login.html", error=error)

@main.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("main.login"))
    return render_template("dashboard.html")

@main.route("/change-password", methods=["GET", "POST"])
def change_password():
    if "user" not in session:
        return redirect(url_for("main.login"))
    error = None
    message = None
    if request.method == "POST":
        old = request.form["old_password"]
        new = request.form["new_password"]
        confirm = request.form["confirm_password"]
        username = session["user"]
        if users[username] != old:
            error = "舊密碼錯誤"
        elif new != confirm:
            error = "新密碼不一致"
        else:
            users[username] = new
            message = "密碼更新成功！"
    return render_template("change-password.html", error=error, message=message)

@main.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("main.login"))
