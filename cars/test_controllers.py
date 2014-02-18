from __future__ import with_statement

from . import app
from .models import User, Car

app.testing = True
app.config['WTF_CSRF_ENABLED'] = False
client = app.test_client()


def teardown_function(function):
    Car.drop_collection()
    User.drop_collection()


def login(email, password):
    return client.post('/login', data=dict(
        email=email,
        password=password
    ), follow_redirects=True)


def logout():
    return client.get('/logout', follow_redirects=True)


def test_add_user_wrong_password():
    user_data = {'name': 'Jhon Doe', 'email': 'jhon@doe.com',
                 'password': 'jJdD', 'confirm': 'jJxx'}
    response = client.post('/users', data=user_data)
    assert b'Passwords must match' in response.data


user_data = {'name': 'Jhon Doe', 'email': 'jhon@doe.com',
             'password': 'jJdD', 'confirm': 'jJdD'}


def test_add_user():
    response = client.post('/users', data=user_data, follow_redirects=True)
    assert b'Thanks for registering' in response.data


def test_login():
    res = client.post('/users', data=user_data, follow_redirects=True)
    assert b'Thanks for registering' in res.data
    response = login('jhon@doe.com', 'jJdD')
    assert b'You were logged in' in response.data


def test_login_user_invalid():
    res = client.post('/users', data=user_data, follow_redirects=True)
    assert b'Thanks for registering' in res.data
    response = login('invalid', 'jJdD')
    assert b'Invalid username or password' in response.data


def test_login_pass_invalid():
    res = client.post('/users', data=user_data, follow_redirects=True)
    assert b'Thanks for registering' in res.data
    response = login('jhon@doe.com', 'invalid')
    assert b'Invalid username or password' in response.data


def test_logout():
    r = client.post('/users', data=user_data, follow_redirects=True)
    assert b'Thanks for registering' in r.data
    res = login('jhon@doe.com', 'jJdD')
    assert b'You were logged in' in res.data
    response = logout()
    assert b'You were logged out' in response.data


def test_add_car():
    car_data = {'year': '1938', 'manufacturer': 'Volkswagen',
                'model': 'Beetle'}
    r = client.post('/users', data=user_data, follow_redirects=True)
    assert b'Thanks for registering' in r.data
    res = login('jhon@doe.com', 'jJdD')
    assert b'You were logged in' in res.data
    with open('cars/data/photo.jpg', 'rb') as f:
        car_data['photo'] = f
        response = client.post('/cars', data=car_data, follow_redirects=True)
        assert b'New car added' in response.data


def test_add_car_missing_file():
    car_data = {'year': '1938', 'manufacturer': 'Volkswagen',
                'model': 'Beetle'}
    r = client.post('/users', data=user_data, follow_redirects=True)
    assert b'Thanks for registering' in r.data
    res = login('jhon@doe.com', 'jJdD')
    assert b'You were logged in' in res.data
    response = client.post('/cars', data=car_data, follow_redirects=True)
    assert b'This field is required' in response.data


def test_add_invalid_file():
    car_data = {'year': '1938', 'manufacturer': 'Volkswagen',
                'model': 'Beetle'}
    r = client.post('/users', data=user_data, follow_redirects=True)
    assert b'Thanks for registering' in r.data
    res = login('jhon@doe.com', 'jJdD')
    assert b'You were logged in' in res.data
    with open('cars/data/text.txt') as f:
        car_data['photo'] = f
        response = client.post('/cars', data=car_data)
        assert b'Only images allowed' in response.data
