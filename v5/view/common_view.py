from flask import Blueprint, render_template, request, redirect, url_for
from db.service.execute_sql_service.UserSQLBuilder import UserSQLBuilder
from domain.user import User
from flask_bcrypt import generate_password_hash

common_bp = Blueprint('common', __name__)
user_service = UserSQLBuilder()

@common_bp.route("/")
def home():
    # response = render_template("contents/home.html")
    response = render_template("contents/common/common_home.html")
    return response

@common_bp.route("/order-type")
def order_type() :
    response = render_template("contents/common/order_type.html")
    return response

@common_bp.route("/order")
def order() :
    response = render_template("contents/common/order.html")
    return response

@common_bp.route("/sign-up", methods = ['GET', 'POST'])
def sign_up() :
    response = None
    if request.method == 'GET' :
        response = render_template("contents/common/sign_up.html")

    elif request.method == 'POST' :
        # form value
        login_id = request.form['login_id'].strip()
        login_pwd = request.form['login_pwd'].strip()
        name = request.form['name'].strip()
        gender =  request.form['gender']
        birthdate =  request.form['birthdate']
        address =  request.form['address'].strip()

        is_empty = False # 유효성 검사
        is_empty_list = [(len(name) == 0), (len(address) == 0), (len(login_id) == 0), (len(login_pwd) == 0)]

        for form_data in is_empty_list : 
            if form_data :
                is_empty = True

        if is_empty :
            response = render_template("contents/common/sign_up.html", is_empty = is_empty)
        else : 
            hashed_login_pwd =  generate_password_hash(login_pwd).decode('utf-8')
            user = User(login_id, hashed_login_pwd, name, gender, birthdate, address, 2) # user domain init, 2 == user_auth(Memeber)
            user_id = user_service.create(user) # user create service, uuid get
            regist_status = True # 등록 여부

            response = redirect(url_for('user.user_board_detail', id = user_id, regist_status = regist_status))

    return response
