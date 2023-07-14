from flask import Blueprint, Flask, render_template, request, redirect, url_for

from view.paging import get_page_info
from service.execute_sql_service.item_execute_sql_service import ItemExecuteSQLService
from domain.item import Item

item_bp = Blueprint('item', __name__, url_prefix='/item')
item_service = ItemExecuteSQLService()

@item_bp.route("/board/list")
def item_board_list():
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    name = request.args.get("name", type=str, default=" ").strip()
    unit_price = request.args.get("unit_price", type=int)
    
    result = []
    if (not name and not unit_price) :
        result = item_service.read_all()
    else :
        result = item_service.read_kwargs(like_name=name, unit_price=unit_price)

    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("contents/board/item_list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num, name=name, unit_price = unit_price)
    return response


@item_bp.route("/board/detail")
def item_board_detail():
    #log
    print('----------------------------view-item : @item_bp.route("/item/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    regist_status = request.args.get("regist_status", type=bool, default=False)

    #service호출
    data = item_service.read_id(id)

    #응답
    response = render_template("contents/board/item_detail.html", data = data, regist_status = regist_status)
    return response

# --------------------------------------------------------register-----------------------------------------------------------------
@item_bp.route("/register", methods = ['GET', 'POST'])
def item_register():
    response = None
    if request.method == 'GET' :
        #log
        print('----------------------------view-item : @item_bp.route("/register", methods = ["GET"])')
        #응답
        response = render_template("contents/register/item_register.html")

    elif request.method == 'POST' :
        #log
        print('----------------------------view-item : @item_bp.route("/register", methods = ["POST"])')
        
        # form value
        name =  request.form['name'].strip()
        type_ =  request.form['type']
        unit_price =  request.form['unit_price'].strip()

        # 유효성 검사
        is_empty = False
        type_positive_match = False

        # 정상적인 숫자값이 들어왔는지 검사
        try :
            if int(unit_price) <= 0 :
                type_positive_match = True
                #log
                print('---------------------------type_positive_match : 음수값이 데이터로 들어옴')
        except ValueError : 
                type_positive_match = True
                #log
                print('----------------------------type_positive_match : 문자열 또는 실수 데이터가 들어옴')

        is_empty_list = [(len(name) == 0), (len(type_) == 0), (len(unit_price) == 0), type_positive_match]

        for form_data in is_empty_list : 
            if form_data :
                is_empty = True

        if is_empty :
            response = render_template("contents/item/register.html", is_empty = is_empty)
        else : 
            # mk name ex: Americano Coffee
            name = name + " " +type_

            # item domain init
            item = Item(name, type_, unit_price)

            # item create service, uuid get
            item_id = item_service.create(item)
            
            # 등록 여부
            regist_status = True

            #응답
            response = redirect(url_for('item.item_board_detail', id = item_id, regist_status = regist_status))

    return response