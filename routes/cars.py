# TODO
from flask import Blueprint


car_router = Blueprint('cars', __name__, url_prefix='/api/cars')


@car_router.route('/', methods=['POST'])
def car_list():
    pass  # return one atribute of each car and can have amount limit


@car_router.route('/image/<id>', methods=['POST'])
def car_image(id):
    pass


@car_router.route('/filter', methods=['POST'])
def api_car_filter():
    pass
