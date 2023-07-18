from flask import Blueprint, Flask, render_template, request, redirect, url_for

from view.paging import get_page_info
from db.service.execute_sql_service.StoreSQLBuilder import StoreSQLBuilder
from domain.store import Store

store_bp = Blueprint('store', __name__, url_prefix='/store')
store_service = StoreSQLBuilder()

@store_bp.route("/board/list")
def store_board_list():
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    name = request.args.get("name", type=str, default=" ").strip()
    address = request.args.get("address", type=str, default=" ").strip()
    
    result = []
    if (not name and not address) :
        result = store_service.read_all("store")
    else :
        result = store_service.read_kwargs("store", like_name = name, like_address = address)

    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("contents/board/store_list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num, name = name, address = address)
    return response


@store_bp.route("/board/detail")
def store_board_detail():
    # parameter value
    id = request.args.get("id", type=str)
    regist_status = request.args.get("regist_status", type=bool, default=False)
    date = request.args.get("date", type=str)

    data = store_service.read_id("store", id) # 1. store detail
    sale_datas = [] # 2. store monthly sales
    if date :
        sale_datas = store_service.read_sales(id, "daily")
    else :    
        sale_datas = store_service.read_sales(id, "monthly") 
    regular_customers = store_service.read_regular_customer(id) # 3. store regular customer

    response = render_template("contents/board/store_detail.html", data = data, sale_datas = sale_datas, regular_customers = regular_customers, regist_status = regist_status)
    return response

# --------------------------------------------------------register-----------------------------------------------------------------
@store_bp.route("/register", methods = ['GET', 'POST'])
def store_register():
    response = None
    if request.method == 'GET' :
        response = render_template("contents/register/store_register.html")

    elif request.method == 'POST' :
        # form value
        type_ =  request.form['type']
        local =  request.form['local'].strip()
        store_num =  request.form['store_num'].strip()
        address =  request.form['address'].strip()

        # 유효성 검사
        is_empty = False
        type_positive_match = False
        try : # 정상적인 숫자값이 들어왔는지 검사
            if int(store_num) <= 0 :
                type_positive_match = True
        except ValueError : 
                type_positive_match = True

        is_empty_list = [(len(local) == 0), (len(address) == 0), (len(store_num) == 0), type_positive_match]

        for form_data in is_empty_list : 
            if form_data :
                is_empty = True

        if is_empty :
            response = render_template("contents/store/register.html", is_empty = is_empty)
        else : 
            name = type_ + " " + local + str(store_num)+"호점" # mk name ex: 스타벅스 홍대8호점
            store = Store(name, type_, address) # store domain init
            store_id = store_service.create(store) # store create service, uuid get
            regist_status = True# 등록 여부

            response = redirect(url_for('store.store_board_detail', id = store_id, regist_status = regist_status))

    return response
