from flask import Blueprint
from flask import request, jsonify
import jwt
import datetime
import os

auth_router = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_router.post("/login")
def login():
    auth_data = request.get_json()
    username = auth_data.get('username')
    password = auth_data.get('password')

    if username == "test" and password == "password":  # TODO use db
        token = jwt.encode({
            'user': username,
            'session_id': "",  # TODO get from db
            'exp': datetime.datetime.now() + datetime.timedelta(hours=1)
        }, "secret", algorithm="HS256")  # TODO use db for secret key
        # TODO save token in db
        response = jsonify({'message': "sucsess"})
        response.set_cookie('token', token, httponly=True,
                            secure=True, samesite='Strict')
        return response

    return jsonify({'message': 'Invalid credentials'}), 401


@auth_router.post("/signup")
def signup():
    return ""


@auth_router.post("/logout")
def logout():
    # TODO remove token from db and set data in session db
    response = jsonify({'message': "sucsess"})
    response.set_cookie('token', "", httponly=True,
                        secure=True, samesite='Strict')
    return response


@auth_router.post("/forgotpassword")
def forgotpassword():
    return ""


@auth_router.post("/resetpassword/<code>")
def resetpassword(code):
    return ""


@auth_router.post("/mfa/set")
def mfa_set():
    return ""


@auth_router.post("/mfa/check")
def mfacheck():
    return ""
