from flask import Blueprint

order_router = Blueprint('order', __name__, url_prefix='/api/basket')


@order_router.route('/add', methods=['POST'])
def api_basket_add():
    pass
    # data = request.json
    # print(data)
    # return jsonify(data)


@order_router.route('/remove', methods=['POST'])
def api_basket_remove():
    pass


@order_router.route('/update', methods=['POST'])
def api_basket_update():
    pass
