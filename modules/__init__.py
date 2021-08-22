from modules.machine import *
from modules.security import *
from modules.constant import *
from modules.database import *

from jwt import decode
from flask import Flask, request
app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET




