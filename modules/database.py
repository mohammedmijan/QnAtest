from flask_pymongo import PyMongo
from flask import Flask
from bson.json_util import loads, dumps
from modules.constant import *

app = Flask(__name__)
app.config["MONGO_URI"] = f"mongodb+srv://{SERVER['name']}:{SERVER['password']}@cluster0.fo82u.mongodb.net/qNaandFaQs"
mongo = PyMongo(app)


def question_server(user,question=None):
    if question:
        json_question = {"user":user, "question":question, "answer":None}
        mongo.db.question.insert_one(json_question)
        response =  {"success":True}
    else:
        questions = mongo.db.question.find({"user": user})
        questions = loads(dumps(questions))
        response = {"success":True,"questions":[quest["question"] for quest in questions],
         "answer":[quest["answer"] for quest in questions ] } 
    return response

