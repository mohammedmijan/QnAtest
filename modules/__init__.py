from modules.machine import *
from modules.security import *
from modules.constant import *
from modules.database import *
from modules.machine import *


from flask_cors import cross_origin, CORS
from jwt import decode
from flask import Flask, request
app = Flask(__name__)
CORS(app=app)
app.config["SECRET_KEY"] = SECRET_KEY




