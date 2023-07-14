from flask import Blueprint, Flask, render_template, request

from view.paging import get_page_info
from service.execute_sql_service.order_execute_sql_service import OrderExecuteSQLService

order_bp = Blueprint('order', __name__, url_prefix='/order')
order_service = OrderExecuteSQLService()

@order_bp.route("/board/list")
def order_board_list():
    #log
    print('----------------------------view-order : @order_bp.route("/order/board/list")')
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    order_at = request.args.get("order_at", type=str, default="no search")
    # result
    result = []
    if order_at == 'no search' :
        result = order_service.read_all()
    elif (len(order_at) != 0) :
        result = order_service.read_order_date(order_at)

    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("contents/board/order_list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num, order_at = order_at)
    return response


@order_bp.route("/board/detail")
def order_board_detail():
    #log
    print('----------------------------view-order : @order_bp.route("/order/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    #service호출
    data = order_service.read_id(id)

    #응답
    response = render_template("contents/board/order_detail.html", data = data)
    return response
