from flask import Blueprint, render_template, request, redirect, url_for, flash, session

main = Blueprint("main", __name__)

# ✅ 登入頁面：設為首頁
@main.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # ✅ 簡易帳密驗證（建議改用資料庫查詢 + 密碼雜湊）
        if username == "admin" and password == "password":
            session["user"] = username
            return redirect(url_for("main.dashboard"))

        flash("Invalid credentials")
    return render_template("login.html")

# ✅ 儀表板頁面：登入後才能看
@main.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("main.login"))
    return render_template("dashboard.html")

# ✅ 管理控制面板（Access Panel）：登入後才能看
@main.route("/access-panel")
def access_panel():
    if "user" not in session:
        return redirect(url_for("main.login"))
    return render_template("access-panel.html")

# ✅ 登出功能
@main.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("main.login"))

