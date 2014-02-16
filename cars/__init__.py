from flask import Flask

from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "cars"}
app.config["SECRET_KEY"] = "super_secret_key"

db = MongoEngine(app)

from . import controllers

__version__ = '0.1'
