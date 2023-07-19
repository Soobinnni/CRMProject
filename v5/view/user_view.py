from flask import Blueprint, render_template, request, redirect, url_for

from view.paging import get_page_info
from db.service.execute_sql_service.UserSQLBuilder import UserSQLBuilder
from domain.user import User

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_service = UserSQLBuilder()
# --------------------------------------------------------board-----------------------------------------------------------------
@user_bp.route("/board/list")
def user_board_list():
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    name = request.args.get("name", default=" ", type=str).strip()
    gender = request.args.get("gender", default=" ", type=str).strip()

    board_num = 10
    result = []
    total_page = 0

    # service
    if( not name and not gender ) :
        result, total_page = user_service.read_all("user", board_num, ((page_num-1)*board_num))
    else : 
        result, total_page = user_service.read_kwargs("user", board_num, ((page_num-1)*board_num), like_name = name, like_gender = gender) 

    page_list = get_page_info(page_num, 5, total_page)

    response = render_template("contents/board/user_list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=result, page_num=page_num, name=name, gender=gender)
    return response

@user_bp.route("/board/detail")
def user_board_detail():
    # parameter value
    id = request.args.get("id", type=str)
    regist_status = request.args.get("regist_status", type=bool, default=False)

    #service   
    user_data = user_service.read_id("user", id) # 1. user detail
    user_order_data = user_service.read_order(id) # 2. user order
    user_visit_store_top_five_data = user_service.read_visit_store_top_five(id) # 3. user visit store top five
    user_purchase_item_top_five_data = user_service.read_purchase_item_top_five(id) # 4. user purchase item top five

    response = render_template("contents/board/user_detail.html", user_data = user_data, user_order_data = user_order_data, user_visit_store_top_five_data = user_visit_store_top_five_data, user_purchase_item_top_five_data = user_purchase_item_top_five_data, regist_status = regist_status )
    return response
# --------------------------------------------------------register-----------------------------------------------------------------
@user_bp.route("/register", methods = ['GET', 'POST'])
def user_register():
    response = None
    if request.method == 'GET' :
        response = render_template("contents/register/user_register.html")

    elif request.method == 'POST' :
        # form value
        name = request.form['name'].strip()
        gender =  request.form['gender']
        birthdate =  request.form['birthdate']
        address =  request.form['address'].strip()

        is_empty = False # 유효성 검사
        is_empty_list = [(len(name) == 0), (len(address) == 0)]

        for form_data in is_empty_list : 
            if form_data :
                is_empty = True

        if is_empty :
            response = render_template("contents/register/user_register.html", is_empty = is_empty)
        else : 
            user = User(name, gender, birthdate, address) # user domain init
            user_id = user_service.create(user) # user create service, uuid get
            regist_status = True # 등록 여부

            response = redirect(url_for('user.user_board_detail', id = user_id, regist_status = regist_status))

    return response

