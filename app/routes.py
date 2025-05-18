from flask import Blueprint, render_template, request, redirect, url_for, flash, session

main = Blueprint("main", __name__)

# ✅ 登入頁面（設為首頁）
@main.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # 🔒 簡化驗證，建議未來改查資料庫與密碼雜湊驗證
        if username == "admin" and password == "password":
            session["user"] = username
            return redirect(url_for("main.dashboard"))

        flash("Invalid credentials")
    return render_template("login.html")

# ✅ 儀表頁（登入後才能訪問）
@main.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("main.login"))
    return render_template("dashboard.html")

# ✅ 管理頁面（登入後才能訪問）
@main.route("/access-panel")
def access_panel():
    if "user" not in session:
        return redirect(url_for("main.login"))
    return render_template("access-panel.html")

# ✅ 登出
@main.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("main.login"))


