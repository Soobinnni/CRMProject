from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required

from view.paging import get_page_info
from db.service.execute_sql_service.UserSQLBuilder import UserSQLBuilder

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_service = UserSQLBuilder()

# --------------------------------------------------------board-----------------------------------------------------------------
@user_bp.route("/board/list")
@login_required
def user_board_list():
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    name = request.args.get("name", default=" ", type=str).strip()
    gender = request.args.get("gender", default=" ", type=str).strip()

    board_num = 10
    result = []
    data_num = 0

    # service
    if( not name and not gender ) :
        result, data_num = user_service.read_all("user", board_num, ((page_num-1)*board_num))
    else : 
        result, data_num = user_service.read_kwargs("user", board_num, ((page_num-1)*board_num), like_name = name, like_gender = gender) 

    page_list, total_page = get_page_info(page_num, 5, data_num, board_num)

    response = render_template("contents/user/list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=result, page_num=page_num, name=name, gender=gender)
    return response

@user_bp.route("/board/detail")
@login_required
def user_board_detail():
    # parameter value
    id = request.args.get("id", type=str)
    regist_status = request.args.get("regist_status", type=bool, default=False)

    #service   
    user_data = user_service.read_id("user", id) # 1. user detail
    user_order_data = user_service.read_order(id) # 2. user order
    user_visit_store_top_five_data = user_service.read_visit_store_top_five(id) # 3. user visit store top five
    user_purchase_item_top_five_data = user_service.read_purchase_item_top_five(id) # 4. user purchase item top five

    response = render_template("contents/user/detail.html", user_data = user_data, user_order_data = user_order_data, user_visit_store_top_five_data = user_visit_store_top_five_data, user_purchase_item_top_five_data = user_purchase_item_top_five_data, regist_status = regist_status )
    return response

@user_bp.route("/order")
@login_required
def order() :
    return render_template('contents/user/order.html')
