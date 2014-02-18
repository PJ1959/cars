from datetime import datetime

from flask import url_for

from . import db


class User(db.Document):
    authenticated = db.BooleanField(default=False, required=False)
    email = db.StringField(primary_key=True, required=True)
    name = db.StringField(max_length=64, required=True)
    password = db.StringField(max_length=128, required=True)
    created = db.DateTimeField(default=datetime.now, required=True)

    def get_absolute_url(self):
        return url_for('users', email=self.email)

    def __unicode__(self):
        return self.name

    def is_active(self):
        return True

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email


class Car(db.Document):
    manufacturer = db.StringField(max_length=128, required=True)
    model = db.StringField(max_length=128, required=True)
    year = db.IntField(required=True)
    photo = db.StringField(max_length=128)

    def edit_absolute_url(self):
        return url_for('edit', id=self.id)

    def delete_absolute_url(self):
        return url_for('delete', id=self.id)

    def __unicode__(self):
        return self.model

    meta = {
        'indexes': ['manufacturer', 'model', 'year'],
        'ordering': ['-year']
    }
