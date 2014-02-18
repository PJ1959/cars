from . import app
from .models import User, Car

app.testing = True
app.config['WTF_CSRF_ENABLED'] = False
app.config['MONGODB_SETTINGS'] = {'DB': 'test_cars_models'}
client = app.test_client()


def teardown_function(function):
    Car.drop_collection()
    User.drop_collection()


def test_add_car():
    c = Car(year='1938', manufacturer='Volkswagen', model='Beetle',
            photo='data/photo.jpg')
    c.save()
    assert Car.objects(year='1938').count() == 1


"""
def test_car_url():
    c = Car(year=1938, manufacturer='Volkswagen', model='Beetle',
            photo='data/photo.jpg')
    c.save()
    assert c.get_absolute_url() == '/cars/beetle'
"""


def test_add_user():
    u = User(name='Jhon Doe', email='jhon@doe.com', password='jJ@dD')
    u.save()
    assert User.objects(email='jhon@doe.com').count() == 1


"""
def test_user_url():
    u = User(name='Jhon Doe', email='jhon@doe.com', password='jJ@dD')
    u.save()
    assert u.get_absolute_url() == '/users/jhon@doe.com'
"""
