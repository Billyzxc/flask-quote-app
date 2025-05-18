from flask import Blueprint, render_template, request, redirect, session, url_for
from datetime import datetime

main = Blueprint('main', __name__)

USERNAME = 'admin'
PASSWORD = '8888'

@main.route('/access-panel', methods=['GET', 'POST'])  # 自訂登入路徑
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('main.home'))
        else:
            return render_template('login.html', error="帳號或密碼錯誤", year=datetime.now().year)
    return render_template('login.html', year=datetime.now().year)

@main.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('main.login'))

@main.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('main.login'))
    return render_template('home.html')
