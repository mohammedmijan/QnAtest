from modules import *

@app.route("/")
def main(): 
    dict1 = { "message" : "Welcome to QnA of Acrylic"}
    return jsoni_cookie(dict1)


@app.route("/submit_question", methods=["POST"])
@cross_origin()
def submit_question():
    question_encoded = request.get_json(force=True)
    token = question_encoded["token"]
    try:
        decode(token, SECRET_KEY, algorithms=["HS256"])
        q_to_database = question_server(user="Null",question=token)
        response = jsoni_cookie(q_to_database)
    except:
        response = jsoni_cookie(HACKER)
    return response

@app.route("/get_question", methods=["GET"])
@cross_origin()
def get_question():
    try:
        questions = question_server(user="Null")
        response = jsoni_cookie(questions)
    except:
        response = jsoni_cookie(HACKER)
    return response


    
if __name__ =="__main__":
    app.run(host="0.0.0.0", port=4699, debug=True)