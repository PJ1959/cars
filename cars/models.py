from datetime import datetime

from flask import url_for

from . import db


class User(db.Document):
    email = db.StringField(required=True)
    name = db.StringField(max_length=64, required=True)
    password = db.StringField(max_length=128, required=True)
    created = db.DateTimeField(default=datetime.now, required=True)

    def get_absolute_url(self):
        return url_for('users', kwargs={"email": self.email})

    def __unicode__(self):
        return self.name


class Car(db.Document):
    manufacturer = db.StringField(max_length=128, required=True)
    model = db.StringField(max_length=128, required=True)
    year = db.IntField(required=True)
    photo = db.StringField(max_length=128, required=True)

    def get_absolute_url(self):
        return url_for('cars', kwargs={"model": self.model})

    def __unicode__(self):
        return self.model

    meta = {
        'indexes': ['manufacturer', 'model', 'year'],
        'ordering': ['-year']
    }
