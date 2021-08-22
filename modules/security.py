from flask import jsonify, make_response
from jwt import encode
from modules.constant import *

def jsoni_cookie(dict_var):
    jsoni = jsonify(dict_var)
    response = make_response(jsoni)
    cookie = encode({"cookie":COOKIE_CODE}, SECRET)
    response.set_cookie("_set", cookie)
    return response