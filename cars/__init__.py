from flask import Flask

from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'DB': 'cars'}
app.config['SECRET_KEY'] = 'super_secret_key'

db = MongoEngine(app)

lm = LoginManager(app)
lm.init_app(app)
lm.login_view = 'login'

from . import controllers

__version__ = '0.1'
