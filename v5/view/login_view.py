# login_bp.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import logout_user, login_required, login_user
from flask_bcrypt import check_password_hash
from db.service.execute_sql_service.UserSQLBuilder import UserSQLBuilder
from domain.user import AuthUser

login_bp = Blueprint('login', __name__)
user_service = UserSQLBuilder()

@login_bp.route("/login", methods = ['GET', 'POST'])
def login() :
    if request.method == 'GET' : 
        return render_template('contents/login/login.html')
    if request.method == 'POST' :
        login_id = request.form['login_id']
        login_pwd = request.form['login_pwd']

        user = user_service.read_user(login_id)

        if user and check_password_hash(user['login_pwd'], login_pwd):
            user_obj = AuthUser(user['login_id'], user['name'], user['gender'], user['birthdate'], user['age'], user['address'], user['user_auth'])
            login_user(user_obj)  # 사용자를 로그인 시킴

            return redirect(url_for('common.home')) 
        else :
            return render_template('contents/login/login.html', try_login_status = False)

@login_bp.route("/logout", methods = ['POST'])
@login_required
def logout() :
    logout_user() # session 만료
    return redirect(url_for('login.login'))