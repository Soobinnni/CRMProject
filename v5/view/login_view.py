# login_bp.py
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from flask_login import logout_user, login_required, UserMixin, login_user, LoginManager
from flask_bcrypt import check_password_hash
from db.service.execute_sql_service.UserSQLBuilder import UserSQLBuilder

login_bp = Blueprint('login', __name__)
# user_service = UserSQLBuilder()


# class User(UserMixin):
#     def __init__(self, id, name, gender, birthdate, age, address):
#         self.id = id
#         self.name = name
#         self.gender = gender
#         self.birthdate = birthdate
#         self.age = age
#         self.address = address

#     def get_id(self):
#         return self.id

#     def __repr__(self):
#         return f"USER: {self.id} = {self.name}"

# @login_bp.route("/login", methods = ['GET', 'POST'])
# def login() :
#     if request.method == 'GET' : 
#         return render_template('contents/login/login.html')
#     if request.method == 'POST' :
#         login_id = request.form['login_id']
#         login_pwd = request.form['login_pwd']

#         user = user_service.read_kwargs(login_id)

#         if user and check_password_hash(user['login_pwd'], login_pwd):
#             user_obj = User(login_id, user['name'])
#             login_user(user_obj)  # 사용자를 로그인 시킴
#             return redirect(url_for('home')) 
#         else :
#             return render_template('contents/login/login.html', try_login_status = False)


# @login_bp.route("/logout", methods = ['POST'])
# @login_required
# def logout() :
#     logout_user() # session 만료
#     return redirect(url_for('login.login'))

# # LoginManager 초기화 함수
# def init_login_manager(login_manager: LoginManager):
#     @login_manager.user_loader
#     def load_user(user_id):
#         user_info = user_service.read_user(user_id) # execute sql
#         return User(user_info['login_id'], user_info['name'], user_info['gender'], user_info['birthdate'], user_info['age'], user_info['address']) #User init
    