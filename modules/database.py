from flask_pymongo import PyMongo
from flask import Flask
from bson.json_util import loads, dumps
from modules.constant import *
from modules.security import *
import time

app = Flask(__name__)
app.config["MONGO_URI"] = f"mongodb+srv://{SERVER['name']}:{SERVER['password']}@cluster0.fo82u.mongodb.net/qNaandFaQs"
mongo = PyMongo(app)


def question_server(user,question=None):
    if question:
        json_question = {"user":user, "question":question, "answer":None, "time":time.time()}
        mongo.db.question.insert_one(json_question)
        response =  {"success":True}
    else:
        questions = mongo.db.question.find({"user": user})
        questions = loads(dumps(questions))
        question = [ ]
        times = questions[-1]["time"] - questions[-2]["time"]
        print(times/60)
        if times/60 >= 3:
            for quest in questions:
                ques = decode_encode_test(quest["question"])["question"]
                question.append({
                "answer":"I do not know.","question":ques})
            question.reverse()
            response = {"success":True,"questions":question } 
        else:
            response = HACKER

    return response



