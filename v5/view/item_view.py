from flask import Blueprint, Flask, render_template, request, redirect, url_for
from flask_login import login_required

from view.paging import get_page_info
from db.service.execute_sql_service.ItemSQLBuilder import ItemSQLBuilder
from domain.item import Item


item_bp = Blueprint('item', __name__, url_prefix='/item')
item_service = ItemSQLBuilder()

@item_bp.route("/board/list")
@login_required
def item_board_list():
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    name = request.args.get("name", type=str, default=" ").strip()
    unit_price = request.args.get("unit_price", type=int)

    board_num = 10
    result = []
    total_page = 0

    if (not name and not unit_price) :
        result, total_page = item_service.read_all("item", board_num, ((page_num-1)*board_num))
    else :
        result, total_page = item_service.read_kwargs("item", board_num, ((page_num-1)*board_num), like_name=name, unit_price=unit_price)

    page_list = get_page_info(page_num, 5, total_page)

    response = render_template("contents/item/list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=result, page_num=page_num, name=name, unit_price = unit_price)
    return response


@item_bp.route("/board/detail")
@login_required
def item_board_detail():
    # parameter value
    id = request.args.get("id", type=str)
    regist_status = request.args.get("regist_status", type=bool, default=False)

    #service
    data = item_service.read_id("item", id) # 1. item detail 
    monthly_sales = item_service.read_monthly_sales(id) # item monthly sales

    monthly_sales_label = []
    monthly_sales_sale_value = []
    monthly_sales_count_value = []
    for monthly_sale in monthly_sales :
        for key, value in monthly_sale.items() :
            if key == 'Month' : 
                monthly_sales_label.append(value)
            elif key == 'Total Revenue' :
                monthly_sales_sale_value.append(value)
            elif key == 'Item Count' : 
                monthly_sales_count_value.append(value)
    print(monthly_sales_count_value)


    response = render_template("contents/item/detail.html", data = data, monthly_sales = monthly_sales, monthly_sales_label = monthly_sales_label, monthly_sales_sale_value = monthly_sales_sale_value, monthly_sales_count_value = monthly_sales_count_value, regist_status = regist_status)
    return response

# --------------------------------------------------------register-----------------------------------------------------------------
@item_bp.route("/register", methods = ['GET', 'POST'])
@login_required
def item_register():
    response = None
    if request.method == 'GET' :
        response = render_template("contents/item/register.html")

    elif request.method == 'POST' :
        # form value
        name =  request.form['name'].strip()
        type_ =  request.form['type']
        unit_price =  request.form['unit_price'].strip()

        # 유효성 검사
        is_empty = False
        type_positive_match = False

        try :
            if int(unit_price) <= 0 :
                type_positive_match = True
        except ValueError : 
                type_positive_match = True

        is_empty_list = [(len(name) == 0), (len(type_) == 0), (len(unit_price) == 0), type_positive_match]

        for form_data in is_empty_list : 
            if form_data :
                is_empty = True

        if is_empty :
            response = render_template("contents/item/register.html", is_empty = is_empty)
        else : 
            name = name + " " +type_ # mk name ex: Americano Coffee
            item = Item(name, type_, unit_price) # item domain init
            item_id = item_service.create(item) # item create service, uuid get
            regist_status = True # 등록 여부

            response = redirect(url_for('item.item_board_detail', id = item_id, regist_status = regist_status))

    return response