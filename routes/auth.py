from flask import Blueprint

auth_router = Blueprint('auth', __name__, url_prefix='/auth')


@auth_router.post("/login")
def login():
    return "test"


@auth_router.post("/signup")
def signup():
    return ""
