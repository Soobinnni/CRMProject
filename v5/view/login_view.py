from flask import Blueprint, url_for, session, render_template, request, redirect

login_bp = Blueprint('login', __name__, url_prefix= '/member')

@login_bp.route("/login")
def login():
    pass