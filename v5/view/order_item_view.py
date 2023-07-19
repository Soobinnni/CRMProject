from flask import Blueprint, Flask, render_template, request

from view.paging import get_page_info
from db.service.execute_sql_service.OrderItemSQLBuilder import OrderItemSQLBuilder

order_item_bp = Blueprint('order_item', __name__, url_prefix='/order-item')
order_item_service = OrderItemSQLBuilder()

@order_item_bp.route("/board/list")
def order_item_board_list():
    page_num = request.args.get("page_num", type=int, default=1) # parameter values

    board_num = 10
    result = []
    total_page = 0
    
    result, total_page = order_item_service.read_all('order_item', board_num, ((page_num-1)*board_num))   
    page_list = get_page_info(page_num, 5, total_page)

    response = render_template("contents/board/order_item_list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=result, page_num=page_num)
    return response


@order_item_bp.route("/board/detail")
def order_item_board_detail():
    id = request.args.get("id", type=str) # parameter value
    data = order_item_service.read_id('"order"', id) #service
    print(id)
    print(data)
    response = render_template("contents/board/order_item_detail.html", data = data)
    
    return response