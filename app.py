from flask import Flask, jsonify, make_response, request
from modules.constant import COOKIE_CODE, SECRET
from jwt import decode , encode

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET

@app.route("/")
def main():
    response = make_response("It is a backend web app.")
    cookie = encode({"cookie":COOKIE_CODE}, SECRET)
    response.set_cookie("_set", cookie)
    return response

@app.route("/submit_question", methods=["POST"])
def submit_question():
    question_encoded = request.get_json(force=True)
    try:
        decode(question_encoded["token"], SECRET, algorithms=["HS256"])
        json_go_server = {"success":True}
        jsoni = jsonify(json_go_server)
        response = make_response(jsoni)
        cookie = encode({"cookie":COOKIE_CODE}, SECRET, algorithm=["HS256"])
        response.set_cookie("_set", cookie)
    except:
        response = {"success":False,"message":"Sorry, you are a hacker."}
    return response


@app.route("/get_question", methods=["POST"])
def get_question():
    _encoded = request.get_json(force=True)
    try:
        decode(_encoded, SECRET, algorithms=["HS256"])
        questions = "Working on server connection......."
        json_server = {"success":True, "questions":questions}
        jsoni = jsonify(json_server)
        response = make_response(jsoni)
        cookie = encode({"cookie":COOKIE_CODE}, SECRET, algorithm=["HS256"]).decode("utf-8")
        response.set_cookie("_set", cookie)
    except:
        response = {"success":False, "message":"Sorry, you are a hacker."}
    return response


    
if __name__ =="__main__":
    app.run(host="0.0.0.0", port=4699, debug=False)