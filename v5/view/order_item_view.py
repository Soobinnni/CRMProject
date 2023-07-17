from flask import Blueprint, Flask, render_template, request

from view.paging import get_page_info
from db.service.execute_sql_service.OrderItemSQLBuilder import OrderItemSQLBuilder

order_item_bp = Blueprint('order_item', __name__, url_prefix='/order-item')
order_item_service = OrderItemSQLBuilder()

@order_item_bp.route("/board/list")
def order_item_board_list():
    page_num = request.args.get("page_num", type=int, default=1) # parameter values

    result = []
    result = order_item_service.read_all('order_item')   
    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("contents/board/order_item_list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num)
    return response


@order_item_bp.route("/board/detail")
def order_item_board_detail():
    id = request.args.get("id", type=str) # parameter value
    data = order_item_service.read_id('"order"', id) #service
    print(id)
    print(data)
    response = render_template("contents/board/order_item_detail.html", data = data)
    
    return response