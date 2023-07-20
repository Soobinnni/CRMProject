from flask import Blueprint, Flask, render_template, request

from view.paging import get_page_info
from db.service.execute_sql_service.OrderSQLBuilder import OrderSQLBuilder

order_bp = Blueprint('order', __name__, url_prefix='/order')
order_service = OrderSQLBuilder()

@order_bp.route("/board/list")
def order_board_list():
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    order_at = request.args.get("order_at", type=str, default=" ").strip()
    
    board_num = 10
    result = []
    total_page = 0

    if not order_at :
        result, total_page = order_service.read_all('"order"', board_num, ((page_num-1)*board_num))
    else :
        result, total_page = order_service.read_kwargs('"order"', board_num, ((page_num-1)*board_num), like_ordered_at = order_at)

    page_list = get_page_info(page_num, 5, total_page)

    response = render_template("contents/order/list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=result, page_num=page_num, order_at = order_at)
    return response


@order_bp.route("/board/detail")
def order_board_detail():
    id = request.args.get("id", type=str) # parameter value
    data = order_service.read_id('"order"', id) #service
    response = render_template("contents/order/detail.html", data = data)
    
    return response
