=====
Django Simple Custom Users
=====

**Note:** Compatible with Postgres Only

django-simple-custom-users is a simple pluggable custom user module for Django.

Quick start
-----------

1. Add "django-simple-custom-users" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'users', # the package name is simply 'users'
    ]

2. Add `AUTH_USER_MODEL = 'users.CustomUser'` to your `settings.py`

3. Run `python manage.py migrate` to create the user model.

And you are ready to use as you please!


Development
-----------
The project for developing and testing this user model is in `djangoproject/`.

Prepare:
A postgres database called `django_simple_custom_users` running at `127.0.0.1:60567`
e.g. `postgres.exe -D 'C:\Program Files\PostgreSQL\12\data'  -h 127.0.0.1 -p 60567`

That database should allow a user called `postgres` to connect with no password. Postgres `trust` auth method in `pg_hba.conf`.

Then start the django project:
```
cd djangoproject/
pip install requirements.txt
python manage.py migrate
python manage.py runserver
```


NOTE: Build with `python setup.py sdist`