from __future__ import with_statement

import cars


client = cars.app.test_client()

car_data = {'year': '1938', 'manufacturer': 'Volkswagen', 'model': 'Beetle'}
with open('cars/data/photo.jpg') as f:
    car_data['photo'] = f

user_data = {'name': 'Jhon Doe', 'email': 'jhon@doe.com',
             'password': 'jJdD', 'confirm': 'jJdD'}


def test_add_car():
    response = client.post('/cars', data=car_data)
    assert b'OK' in response.data


def test_add_missing_file():
    car_data['photo'] = 'missing'
    response = client.post('/cars', data=car_data)
    assert b'invalid' in response.data


def test_add_invalid_file():
    with open('data/text.txt') as f:
        car_data['photo'] = f
        response = client.post('/cars', data=car_data)
        assert b'invalid' in response.data


def test_list_car():
    response = client.get('/cars')
    assert b'OK' in response.data


def test_add_user():
    response = client.post('/users', data=user_data)
    assert b'OK' in response.data


def test_add_user_wrong_password():
    user_data['confirm'] = 'jJjJ'
    response = client.post('/users', data=user_data)
    assert b'invalid' in response.data


def login(username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def logout():
    return client.get('/logout', follow_redirects=True)


def test_login_logout():
    response = login('admin', 'default')
    assert 'You were logged in' in response.data
    response = logout()
    assert 'You were logged out' in response.data
    response = login('adminx', 'default')
    assert 'Invalid username or password' in response.data
    response = login('admin', 'defaultx')
    assert 'Invalid username or password' in response.data
