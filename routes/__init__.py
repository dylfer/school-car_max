from .auth import router as auth_router
from .genral import router as genral_router
from .order import router as order_router


def register_routes(app):
    app.register_blueprint(auth_router)
    app.register_blueprint(genral_router)
    app.register_blueprint(order_router)
