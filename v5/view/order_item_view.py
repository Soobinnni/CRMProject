from flask import Blueprint, Flask, render_template, request

from view.paging import get_page_info
from service.execute_sql_service.order_item_execute_sql_service import OrderItemExecuteSQLService

order_item_bp = Blueprint('order_item', __name__, url_prefix='/order-item')
order_item_service = OrderItemExecuteSQLService()

@order_item_bp.route("/board/list")
def order_item_board_list():
    page_num = request.args.get("page_num", type=int) # parameter values

    result = []
    result = order_item_service.read_all()   
    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("contents/board/order_item_list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num)
    return response


@order_item_bp.route("/board/detail")
def order_item_board_detail():
    #log
    print('----------------------------view-order-item : @order_item_bp.route("/order-item/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    #service호출
    data = order_item_service.read_id(id)

    #응답
    response = render_template("contents/board/order_item_detail.html", data = data)
    return response