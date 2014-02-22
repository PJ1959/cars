Cars catalog
============

[![Build Status](https://travis-ci.org/wiliamsouza/cars.png?branch=master)](https://travis-ci.org/wiliamsouza/cars)

A car application writen using Flask and MongoDB.

Get code
--------

```
git clone https://github.com/wiliamsouza/cars.git
```

Requirements
------------

```
pip install -r requirements.txt
```

Search
------

Enable full text search and create index.

```
mongo
use cars
db.adminCommand( { setParameter : 1, textSearchEnabled : true } )
db.car.ensureIndex( { manufacturer: "text", model: "text", year: "text" } );
```

Configuration
-------------

Before run development server or tests ensure you have changed `UPLOAD_FOLDER`
to the full path of the project `.../cars/cars/data/images`. The default path
point to deploy folder `/srv/cars/cars/data/images`. It's is located at
`cars/__init__.py`:

```
UPLOAD_FOLDER = '/srv/cars/cars/data/images'
```

Running development server
--------------------------

```
python manage.py runserver
```

Open your browser [http://0.0.0.0:5000/](http://0.0.0.0:5000/).

Running tests
-------------

First things first! **Enable MongoDB full text search and create indexes** [here](#Search)

Cars use [pyenv](https://github.com/yyuu/pyenv) to handle multiple python
versions install it before run `tox`.

```
pyenv install 2.6.9
pyenv install 2.7.6
pyenv install 3.3.4
pyenv install pypy-2.2.1
pyenv rehash
```

Run tox:

```
tox
```

`tox` will run tests agains python versions 2.6.9, 2.7.6, 3.3.4 and pypy 2.2.1

Or use `setup.py`:

```
python setup.py test
```

Deploy
======

Apache mod-wsgi
---------------

```
# apt-get install libapache2-mod-wsgi

```

MongoDB
-------

Follow the official [MongoDB instructions](http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/#install-mongodb)

Remember! after the installation, **Enable MongoDB full text search and create indexes** [here](#Search)

Code
----

```
# apt-get install git
# apt-get install python-virtualenv
# cd /srv
# git clone https://github.com/wiliamsouza/cars.git
# chown -R ubuntu.ubuntu cars/
# cd cars
virtualenv .
source bin/activate
pip install -r requirements.txt
```

Enable application
------------------

With `root` user run:

```
# cp etc/apache2/sites-available/cars /etc/apache2/sites-available/cars
# a2dissite default
# a2ensite cars
```
