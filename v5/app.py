from flask import Flask, request, render_template, url_for, redirect
import os
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import bcrypt
import sqlite3

from view.user_view import user_bp
from view.item_view import item_bp
from view.order_view import order_bp
from view.order_item_view import order_item_bp
from view.store_view import store_bp
from view.common_view import common_bp
from view.login_view import login_bp

app = Flask(__name__)

# ---------------------------------------------login---------------------------------------------------------------
app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)
DATABASE = 'db/crm.db'

class User(UserMixin):
    def __init__(self, login_id, name, login_pwd):
        self.login_id = login_id
        self.name = name
        self.login_pwd = login_pwd

    def check_password(self, login_pwd):
        return bcrypt.checkpw(login_pwd.encode('utf-8'), self.login_pwd)
    
    def __repr__(self): # cf. toString()
        return f"User(login_id={self.login_id}, name='{self.name}')"
    
def get_user_by_id(login_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE login_id=?", (login_id,))
    user_data = cursor.fetchone()
    conn.close()
    if user_data:
        login_id, username, password = user_data
        return User(login_id, username, password)
    return None

login_manager = LoginManager()
login_manager.login_view = 'login.login'

@login_manager.user_loader
def load_user(login_id):
    return get_user_by_id(login_id)
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