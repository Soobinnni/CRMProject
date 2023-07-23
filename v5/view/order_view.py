from flask import Blueprint, render_template, request, session
from flask_login import login_required, current_user

from view.paging import get_page_info
from db.service.execute_sql_service.OrderSQLBuilder import OrderSQLBuilder
from db.service.execute_sql_service.StoreSQLBuilder import StoreSQLBuilder
from db.service.execute_sql_service.ItemSQLBuilder import ItemSQLBuilder

from domain.order import Order

order_bp = Blueprint('order', __name__, url_prefix='/order')
order_service = OrderSQLBuilder()

@order_bp.route("/board/list")
@login_required
def order_board_list():
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    order_at = request.args.get("order_at", type=str, default=" ").strip()
    
    board_num = 10
    result = []
    data_num = 0

    if not order_at :
        result, data_num = order_service.read_all('"order"', board_num, ((page_num-1)*board_num))
    else :
        result, data_num = order_service.read_kwargs('"order"', board_num, ((page_num-1)*board_num), like_ordered_at = order_at)

    page_list, total_page = get_page_info(page_num, 5, data_num, board_num)

    response = render_template("contents/order/list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=result, page_num=page_num, order_at = order_at)
    return response


@order_bp.route("/board/detail")
@login_required
def order_board_detail():
    id = request.args.get("id", type=str) # parameter value
    data = order_service.read_id('"order"', id) #service
    response = render_template("contents/order/detail.html", data = data)
    
    return response


@order_bp.route("/store-select")
# @login_required
def store_select():
    store_service = StoreSQLBuilder()
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    store_type = request.args.get("store_type", type=str, default=" ").strip()
    gu = request.args.get("gu", type=str, default=" ").strip()
    nav_type = request.args.get("nav_type", type=str, default="brand").strip()

    board_num = 12
    result = []
    data_num = 0
    user_id = ""

    if current_user.is_authenticated : # 회원 주문
        user_id = current_user.uuid
    session['order'] = {'user_id' : user_id }

    if (not store_type and not gu) : 
        result, data_num = store_service.read_all("store", board_num, ((page_num-1)*board_num))
    else :
        result, data_num = store_service.read_kwargs("store", board_num, ((page_num-1)*board_num), like_name = store_type, like_address = gu)

    store_type_list = [value['type'] for value in store_service.read_type()]

    page_list, total_page = get_page_info(page_num, 3, data_num, board_num)

    response = render_template("contents/order/store-select.html", stores = result, page_num = page_num, page_list = page_list, total_page = total_page, store_type_list = store_type_list, store_type = store_type, gu = gu, nav_type = nav_type)   
    
    return response


@order_bp.route("/<store_id>/item-select")
def item_select(store_id):
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    item_type = request.args.get("item_type", type=str, default=" ").strip()

    order = session.get('order')
    order['store_id'] = store_id

    board_num = 12
    result = []
    data_num = 0
    item_service = ItemSQLBuilder()
    if (not item_type) : 
        result, data_num = item_service.read_all("item", board_num, ((page_num-1)*board_num))
    else :
        result, data_num = item_service.read_kwargs("item", board_num, ((page_num-1)*board_num), like_name = item_type)

    page_list, total_page = get_page_info(page_num, 3, data_num, board_num)
    item_type_list = [value['type'] for value in item_service.read_type()]

    response = render_template("contents/order/item-select.html",store_id = store_id, items = result, page_num = page_num, page_list = page_list, total_page = total_page, item_type_list = item_type_list, item_type = item_type)   
    return response
