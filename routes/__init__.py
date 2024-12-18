from flask import request, jsonify
import jwt
from routes.auth import auth_router
from routes.genral import genral_router
from routes.order import order_router
from routes.cars import car_router


def register_routes(app):

    @app.before_request
    def before_request():
        if request.path in ['/dashboard', "/orders", "/settings", "/bookings"]:
            token = request.cookies.get('token')
            if not token:
                return jsonify({'message': 'Missing token'}), 401
            try:  # TODO get secret from db
                jwt.decode(token, 'secret', algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return jsonify({'message': 'Expired token'}), 401
            except jwt.InvalidTokenError:
                return jsonify({'message': 'Invalid token'}), 401

    app.register_blueprint(auth_router)
    app.register_blueprint(genral_router)
    app.register_blueprint(order_router)
    app.register_blueprint(car_router)
