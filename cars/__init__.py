import os

from flask import Flask

from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager

UPLOAD_FOLDER = '/srv/cars/cars/data/images'
if 'TRAVIS' in os.environ:
    UPLOAD_FOLDER = '{0}/{1}'.format(os.environ['TRAVIS_BUILD_DIR'],
                                     'cars/data/images')

app = Flask(__name__)
#app.config['DEBUG'] = True
app.config['MONGODB_SETTINGS'] = {'DB': 'cars'}
app.config['SECRET_KEY'] = 'super_secret_key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = MongoEngine(app)
db.connection.admin.command('setParameter', textSearchEnabled=True)

lm = LoginManager(app)
lm.init_app(app)
lm.login_view = 'login'

from . import controllers

__version__ = '0.1'
