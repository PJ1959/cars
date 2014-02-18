from werkzeug import secure_filename

from mongoengine import DoesNotExist, MultipleObjectsReturned

from flask import (request, redirect, url_for,
                   render_template, flash)

from flask.ext.login import login_required, logout_user

from . import app, lm
from .models import User, Car
from .forms import RegistrationForm, LoginForm, SearchForm, CarForm


@lm.user_loader
def load_user(email):
    try:
        user = User.objects.get(email=email)
        return user
    except (DoesNotExist, MultipleObjectsReturned):
        return None


@app.route('/', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    cars = None
    if form.validate_on_submit():
        cars = Car.objects(model=form.search.data)
    return render_template('search.html', form=form, cars=cars)


@app.route('/cars', methods=['GET', 'POST'])
@login_required
def cars():
    form = CarForm()
    if form.validate_on_submit():
        if 'photo' in request.files:
            photo = request.files['photo']
            filename = secure_filename(photo.filename)
            photo.save('cars/data/images/{0}'.format(filename))
            car = Car(manufacturer=form.manufacturer.data,
                      model=form.model.data, year=form.year.data,
                      photo=filename)
            car.save()
            flash('New car added')
            return redirect(url_for('search'))
    url = url_for('cars')
    return render_template('cars.html', form=form, url=url)


@app.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    car = Car.objects.get(id=id)
    form = CarForm(obj=car)
    if form.validate_on_submit():
        filename = None
        if 'photo' in request.files:
            photo = request.files['photo']
            filename = secure_filename(photo.filename)
            if filename != '':
                photo.save('cars/data/images/{0}'.format(filename))
                car.photo = filename
        car.manufacturer = form.manufacturer.data
        car.model = form.model.data
        car.year = form.year.data
        car.save()
        flash('Car updated')
        return redirect(car.edit_absolute_url())
    url = car.edit_absolute_url()
    return render_template('cars.html', form=form, url=url)


@app.route('/delete/<id>', methods=['GET'])
@login_required
def delete(id):
    cars = Car.objects.get(id=id)
    cars.delete()
    flash('Car removed')
    return redirect(url_for('search'))


@app.route('/users', methods=['GET', 'POST'])
def users():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, name=form.name.data,
                    password=form.password.data)
        user.save()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('users.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
            flash('You were logged in')
            return redirect(url_for('search'))
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('search'))


if __name__ == '__main__':
    app.run()
