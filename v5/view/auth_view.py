from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import logout_user, login_required, login_user
from flask_bcrypt import check_password_hash

from db.service.execute_sql_service.UserSQLBuilder import UserSQLBuilder
from domain.user import AuthUser

#TODO: Principal객체로 Authorization하기

auth_bp = Blueprint('auth', __name__)
user_service = UserSQLBuilder()

@auth_bp.route("/login", methods = ['GET', 'POST'])
def login() :
    response = None
    
    if request.method == 'GET' : 
        response = render_template('contents/auth/login.html')
    if request.method == 'POST' :
        login_id = request.form['login_id']
        login_pwd = request.form['login_pwd']

        user = user_service.read_user(login_id)

        if user and check_password_hash(user['login_pwd'], login_pwd):
            remember = True if request.form.get('remember') else False # login 유지
            user_obj = AuthUser(user['login_id'], user['name'], user['gender'], user['birthdate'], user['age'], user['address'], user['user_auth'])
            login_user(user_obj, remember=remember) # Authentication

            response = redirect(url_for('user.user_board_list')) if user_obj.user_auth == 'ADMIN' else redirect(url_for('common.home'))

        else :
            response = render_template('contents/auth/login.html', try_login_status = 'fail')
        
    return response

@auth_bp.route("/logout", methods = ['POST'])
@login_required
def logout() :
    logout_user() # session 만료
    return redirect(url_for('auth.login'))