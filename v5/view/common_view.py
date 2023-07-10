from flask import Blueprint, Flask, render_template, request

common_bp = Blueprint('common', __name__)

@common_bp.route("/")
def home():
    response = render_template("home.html")
    return response