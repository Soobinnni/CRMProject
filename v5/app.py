from flask import Flask

from view.user_view import user_bp
from view.item_view import item_bp
from view.order_view import order_bp
from view.order_item_view import order_item_bp
from view.store_view import store_bp
from view.common_view import common_bp

app = Flask(__name__)
# ---------------------------------------------views---------------------------------------------------------------
app.register_blueprint(user_bp)
app.register_blueprint(item_bp)
app.register_blueprint(order_bp)
app.register_blueprint(order_item_bp)
app.register_blueprint(store_bp)
app.register_blueprint(common_bp)   
# -----------------------------------------------Main---------------------------------------------------------------------
if __name__ == "__main__":
    # app.run(port=5003, host = "0.0.0.0")
    app.run(debug=True, port=5003)