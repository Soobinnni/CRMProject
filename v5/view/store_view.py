from flask import Blueprint, Flask, render_template, request, redirect, url_for

from view.paging import get_page_info
from service.execute_sql_service.store_execute_sql_service import StoreExecuteSQLService
from domain.store import Store

store_bp = Blueprint('store', __name__, url_prefix='/store')
store_service = StoreExecuteSQLService()

@store_bp.route("/board/list")
def store_board_list():
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    name = request.args.get("name", type=str, default=" ").strip()
    address = request.args.get("address", type=str, default=" ").strip()
    
    result = []
    if (not name and not address) :
        result = store_service.read_all()
    elif not name :
        result = store_service.read_address(address)
    elif not address :
        result = store_service.read_name(name)
    elif name and address :
        result = store_service.read_name_address(name, address)

    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("contents/board/store_list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num, name = name, address = address)
    return response


@store_bp.route("/board/detail")
def store_board_detail():
    #log
    print('----------------------------view-store : @store_bp.route("/store/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    regist_status = request.args.get("regist_status", type=bool, default=False)
    #service호출
    data = store_service.read_id(id)

    #응답
    response = render_template("contents/board/store_detail.html", data = data, regist_status = regist_status)
    return response

# --------------------------------------------------------register-----------------------------------------------------------------
@store_bp.route("/register", methods = ['GET', 'POST'])
def store_register():
    response = None
    if request.method == 'GET' :
        #log
        print('----------------------------view-store : @store_bp.route("/register", methods = ["GET"])')
        #응답
        response = render_template("contents/register/store_register.html")

    elif request.method == 'POST' :
        #log
        print('----------------------------view-store : @store_bp.route("/register", methods = ["POST"])')
        
        # form value
        type_ =  request.form['type']
        local =  request.form['local'].strip()
        store_num =  request.form['store_num'].strip()
        address =  request.form['address'].strip()

        # 유효성 검사
        is_empty = False
        type_positive_match = False

        # 정상적인 숫자값이 들어왔는지 검사
        try :
            if int(store_num) <= 0 :
                type_positive_match = True
                #log
                print('---------------------------type_positive_match : 음수값이 데이터로 들어옴')
        except ValueError : 
                type_positive_match = True
                #log
                print('----------------------------type_positive_match : 문자열 또는 실수 데이터가 들어옴')

        is_empty_list = [(len(local) == 0), (len(address) == 0), (len(store_num) == 0), type_positive_match]

        for form_data in is_empty_list : 
            if form_data :
                is_empty = True

        if is_empty :
            response = render_template("contents/store/register.html", is_empty = is_empty)
        else : 
            # mk name ex: 스타벅스 홍대8호점
            name = type_ + " " + local + str(store_num)+"호점"

            # store domain init
            store = Store(name, type_, address)

            # store create service, uuid get
            store_id = store_service.create(store)

            # 등록 여부
            regist_status = True

            #응답
            response = redirect(url_for('store.store_board_detail', id = store_id, regist_status = regist_status))

    return response
