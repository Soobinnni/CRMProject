from flask import Flask, request, render_template, url_for, redirect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import os
from flask_bcrypt import check_password_hash
from db.service.execute_sql_service.UserSQLBuilder import UserSQLBuilder

from view.user_view import user_bp
from view.item_view import item_bp
from view.order_view import order_bp
from view.order_item_view import order_item_bp
from view.store_view import store_bp
from view.common_view import common_bp
from view.login_view import login_bp

app = Flask(__name__)
# ---------------------------------------------login---------------------------------------------
app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app) # 서버와 바인딩
login_manager.login_view = 'login.login' # 로그인 처리 지정

# ---------------------------------------------views---------------------------------------------------------------
app.register_blueprint(user_bp)
app.register_blueprint(item_bp)
app.register_blueprint(order_bp)
app.register_blueprint(order_item_bp)
app.register_blueprint(store_bp)
app.register_blueprint(common_bp)
app.register_blueprint(login_bp)

user_service = UserSQLBuilder()

class User(UserMixin):
    def __init__(self, id, name, gender, birthdate, age, address):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.age = age
        self.address = address

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"USER: {self.id} = {self.name}"

@app.route("/login", methods = ['GET', 'POST'])
def login() :
    if request.method == 'GET' : 
        return render_template('contents/login/login.html')
    if request.method == 'POST' :
        login_id = request.form['login_id']
        login_pwd = request.form['login_pwd']

        user = user_service.read_user(login_id)

        if user and check_password_hash(user['login_pwd'], login_pwd):
            user_obj = User(user['login_id'], user['name'], user['gender'], user['birthdate'], user['age'], user['address'])
            login_user(user_obj)  # 사용자를 로그인 시킴

            return redirect(url_for('common.home')) 
        else :
            return render_template('contents/login/login.html', try_login_status = False)

@app.route("/logout", methods = ['POST'])
@login_required
def logout() :
    logout_user() # session 만료
    return redirect(url_for('login.login'))

@login_manager.user_loader
def load_user(user_id):
    user_info = user_service.read_user(user_id) # execute sql
    return User(user_info['login_id'], user_info['name'], user_info['gender'], user_info['birthdate'], user_info['age'], user_info['address']) #User init

# -----------------------------------------------Main---------------------------------------------------------------------
if __name__ == "__main__":
    # app.run(port=5003, host = "0.0.0.0")
    app.run(debug=True, port=8080)