Cars catalog
============

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

Install python versions
-----------------------

```
pyenv install 2.6.9
pyenv install 2.7.6
pyenv install 3.3.4
pyenv install pypy-2.2.1
pyenv rehash
```

```
tox
```

`tox` will run tests agains python2.6.9, python.2.7.6 and python3.3.4

Or use `setup.py`:

```
python setup.py test
```
