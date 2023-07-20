# login_bp.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import logout_user

login_bp = Blueprint('login', __name__)
DATABASE = 'db/crm.db'

@login_bp.route("/login", methods = ['GET', 'POST'])
def login() :
    if request.method == 'GET' : 
        return render_template('contents/member/login.html')
    if request.method == 'POST' :
        pass
    
@login_bp.route("/logout", methods = ['POST'])
def logout() :
    logout_user() # session에 저장된 사용자에 대한 정보가 삭제
    return redirect(url_for('common.home'))