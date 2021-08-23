from flask import jsonify, make_response
from jwt import encode, decode
from modules.constant import *


def jsoni_cookie(dict_var):
    jsoni = jsonify(dict_var)
    response = make_response(jsoni)
    cookie = encode({"cookie":COOKIE_CODE}, SECRET_KEY)
    response.set_cookie("_set", cookie)
    return response

def authenticate_hacker(mail, password, user):
    if mail and password and user:
        pass
    elif mail and password or user and password:
        pass
    return True

def decode_encode_test(var_):
    return decode(var_, SECRET_KEY, algorithms=["HS256"], options={"verify_iat":True, "verify_exp":True})