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

MongoDB
-------

Enable full text search and create index.

```
mongo
use cars
db.adminCommand( { setParameter : 1, textSearchEnabled : true } )
db.car.ensureIndex( { manufacturer: "text", model: "text", year: "text" } );
```

Running development server
--------------------------

```
python manage.py runserver
```

Open your browser [http://0.0.0.0:5000/](http://0.0.0.0:5000/).

Running tests
-------------

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
