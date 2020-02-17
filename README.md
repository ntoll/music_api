# Music API with Django

A very simple API example for the purposes of teaching.

## Setup

Create a new virtualenv, activate it and install the requirements:

```
$ python3 -m venv my_venv
$ source my_venv/bin/activate
$ pip install -r requirements.py
```

Migrate the database:

```
$ python manage.py migrate
```

Create a new admin user:

```
$ python manage.py createsuperuser
```

(Follow the instructions)

Start the server:

```
$ python manage.py runserver
```

Go visit http://127.0.0.1:8000/

## Run the Tests

```
$ python manage.py test
```
