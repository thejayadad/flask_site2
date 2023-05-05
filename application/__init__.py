

from flask import Flask
from flask_pymongo import pymongo
from os import environ


app = Flask(__name__)
app.config["SECRET_KEY"] = "b3712e014745d289d23ac1eaf7968403fefb1549"
app.config["MONGO_URI"] = "mongodb+srv://jaydunb12:Football123@cluster0.develxm.mongodb.net/"





from application import routes




