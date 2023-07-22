from flask import Flask
from flask_login import LoginManager
import os
from db.service.execute_sql_service.UserSQLBuilder import UserSQLBuilder

from view.user_view import user_bp
from view.item_view import item_bp
from view.order_view import order_bp
from view.order_item_view import order_item_bp
from view.store_view import store_bp
from view.common_view import common_bp
from view.login_view import login_bp

from domain.user import AuthUser

app = Flask(__name__)
# ---------------------------------------------login---------------------------------------------
app.secret_key = os.urandom(24)
login_manager = LoginManager(app)
login_manager.login_view = 'login.login' # 로그인 처리 지정
user_service = UserSQLBuilder()

@login_manager.user_loader
def load_user(user_id):
    user_info = user_service.read_user(user_id) # execute sql
    return AuthUser(user_info['login_id'], user_info['name'], user_info['gender'], user_info['birthdate'], user_info['age'], user_info['address'], user_info['user_auth']) #User init
# ---------------------------------------------views---------------------------------------------------------------
app.register_blueprint(user_bp)
app.register_blueprint(item_bp)
app.register_blueprint(order_bp)
app.register_blueprint(order_item_bp)
app.register_blueprint(store_bp)
app.register_blueprint(common_bp)
app.register_blueprint(login_bp)
# -----------------------------------------------Main---------------------------------------------------------------------
if __name__ == "__main__":
    # app.run(port=5003, host = "0.0.0.0")
    app.run(debug=True, port=8080)