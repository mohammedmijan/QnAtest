from flask import jsonify, make_response
from jwt import encode
from modules.constant import *


def jsoni_cookie(dict_var):
    jsoni = jsonify(dict_var)
    response = make_response(jsoni)
    cookie = encode({"cookie":COOKIE_CODE}, SECRET)
    response.set_cookie("_set", cookie)
    return response

def authenticate_hacker(mail, password, user):
    if mail and password and user:
        pass
    elif mail and password or user and password:
        pass
    return True