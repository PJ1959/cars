from werkzeug import secure_filename

from mongoengine import DoesNotExist, MultipleObjectsReturned

from flask import (request, redirect, url_for, render_template,
                   flash, send_from_directory)

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


@app.route('/photos/<path:filename>')
def photos(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    cars = []
    if form.validate_on_submit():
        db = Car._get_db()
        results = db.command("text", "car", search=form.search.data)['results']
        for r in results:
            c = r['obj']
            car = Car()
            car.manufacturer = c['manufacturer']
            car.model = c['model']
            car.year = c['year']
            car.photo = c['photo']
            car.id = c['_id']
            cars.append(car)
    return render_template('search.html', form=form, cars=cars)


@app.route('/cars', methods=['GET', 'POST'])
@login_required
def cars():
    form = CarForm()
    if form.validate_on_submit():
        if 'photo' in request.files:
            photo = request.files['photo']
            filename = secure_filename(photo.filename)
            path = '{0}/{1}'.format(app.config['UPLOAD_FOLDER'], filename)
            photo.save(path)
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
                path = '{0}/{1}'.format(app.config['UPLOAD_FOLDER'], filename)
                photo.save(path)
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
