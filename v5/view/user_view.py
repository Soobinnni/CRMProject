from flask import Blueprint, render_template, request, redirect, url_for

from view.paging import get_page_info
from service.execute_sql_service.user_execute_sql_service import UserService
from domain.user import User

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_service = UserService()
# --------------------------------------------------------board-----------------------------------------------------------------
@user_bp.route("/board/list")
def user_board_list():
    #log
    print('----------------------------view-user : @user_bp.route("/user/board/list")')
    # parameter values
    page_num = request.args.get("page_num", type=int, default=1)
    name = request.args.get("name", default="no search", type=str).strip()
    gender = request.args.get("gender", default="no search", type=str)

    # result
    result = []

    # service
    if( name == 'no search' and gender == 'no search' ):
        result = user_service.read_all()
    elif (len(name) != 0) and (len(gender) != 0) : 
        result = user_service.read_name_gender(name, gender)

    total_page, page_list, page_datas = get_page_info(page_num, 10, 3, result) # 현재 페이지 번호, 노출 게시물 개수, 노출 페이지 간격, 게시물 데이터

    response = render_template("board/user_list.html", datas=result, total_page = total_page, page_list=page_list, page_datas=page_datas, page_num=page_num, name=name, gender=gender)
    return response


@user_bp.route("/board/detail")
def user_board_detail():
    #log
    print('----------------------------view-user : @user_bp.route("/user/board/detail")')
    # parameter value
    id = request.args.get("id", type=str)
    regist_status = request.args.get("regist_status", type=bool, default=False)
    #service호출
    data = user_service.read_id(id)

    #응답
    response = render_template("user/board/detail.html", data = data, regist_status = regist_status )
    return response
# --------------------------------------------------------register-----------------------------------------------------------------
@user_bp.route("/register", methods = ['GET', 'POST'])
def user_register():

    response = None
    if request.method == 'GET' :
        #log
        print('----------------------------view-user : @user_bp.route("/register", methods = ["GET"])')
        #응답
        response = render_template("register/user_register.html")

    elif request.method == 'POST' :
        #log
        print('----------------------------view-user : @user_bp.route("/register", methods = ["POST"])')
        
        # form value
        name = request.form['name'].strip()
        gender =  request.form['gender']
        birthdate =  request.form['birthdate']
        address =  request.form['address'].strip()

        # 유효성 검사
        is_empty = False
        is_empty_list = [(len(name) == 0), (len(address) == 0)]

        for form_data in is_empty_list : 
            if form_data :
                is_empty = True

        if is_empty :
            response = render_template("register/user_register.html", is_empty = is_empty)
        else : 
            # user domain init
            user = User(name, gender, birthdate, address)

            # user create service, uuid get
            user_id = user_service.create(user)

            # 등록 여부
            regist_status = True

            #응답
            response = redirect(url_for('user.user_board_detail', id = user_id, regist_status = regist_status))

    return response

