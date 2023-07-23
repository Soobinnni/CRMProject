from flask import Blueprint, Flask, render_template, request, redirect, url_for
from flask_login import login_required

from view.paging import get_page_info
from db.service.execute_sql_service.StoreSQLBuilder import StoreSQLBuilder
from domain.store import Store

store_bp = Blueprint('store', __name__, url_prefix='/store')
store_service = StoreSQLBuilder()

# --------------------------------------------------------read-----------------------------------------------------------------
@store_bp.route("/board/list")
@login_required
def store_board_list():
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    name = request.args.get("name", type=str, default=" ").strip()
    address = request.args.get("address", type=str, default=" ").strip()

    board_num = 10
    result = []
    data_num = 0
    
    if (not name and not address) :
        result, data_num = store_service.read_all("store", board_num, ((page_num-1)*board_num))
    else :
        result, data_num = store_service.read_kwargs("store", board_num, ((page_num-1)*board_num), like_name = name, like_address = address)

    page_list, total_page = get_page_info(page_num, 5, data_num, board_num)

    response = render_template("contents/store/list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=result, page_num=page_num, name = name, address = address)
    return response

@store_bp.route("/board/detail")
@login_required
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

    response = render_template("contents/store/detail.html", data = data, sale_datas = sale_datas, regular_customers = regular_customers, regist_status = regist_status)
    return response

@store_bp.route("/select")
# @login_required
def select():
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    store_type = request.args.get("store_type", type=str, default=" ").strip()
    gu = request.args.get("gu", type=str, default=" ").strip()
    nav_type = request.args.get("nav_type", type=str, default="brand").strip()

    board_num = 12
    result = []
    data_num = 0

    if (not store_type and not gu) : 
        result, data_num = store_service.read_all("store", board_num, ((page_num-1)*board_num))
    else :
        result, data_num = store_service.read_kwargs("store", board_num, ((page_num-1)*board_num), like_name = store_type, like_address = gu )

    store_type_list = [value['type'] for value in store_service.read_type()]

    page_list, total_page = get_page_info(page_num, 3, data_num, board_num)

    response = render_template("contents/store/select.html", stores = result, page_num = page_num, page_list = page_list, total_page = total_page, store_type_list = store_type_list, store_type = store_type, gu = gu, nav_type = nav_type)
    return response

# --------------------------------------------------------register-----------------------------------------------------------------
@store_bp.route("/register", methods = ['GET', 'POST'])
@login_required
def store_register():
    response = None
    if request.method == 'GET' :
        response = render_template("contents/store/register.html")

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
