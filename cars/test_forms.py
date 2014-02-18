from .forms import RegistrationForm, LoginForm, SearchForm, CarForm

user_data = {'name': 'Jhon Doe', 'email': 'jhon@doe.com',
             'password': 'jJdD', 'confirm': 'jJdD'}

car_data = {'year': '1938', 'manufacturer': 'Volkswagen',
            'model': 'Beetle'}

"""
def test_registration_form():
    form = RegistrationForm()
    form.process(user_data)
    form.validate()
    assert form.errors == {}


def test_login_form():
    form = LoginForm()
    form.process({'username': 'jhon@doe.com', 'password': 'jJdD'})
    form.validate()
    assert form.errors == {}


def test_search_form():
    form = SearchForm()
    form.process({'search': 'Beetle'})
    form.validate()
    assert form.errors == {}


def test_car_form():
    form = CarForm()
    form.process(car_data)
    form.validate()
    assert form.errors == {}
"""
