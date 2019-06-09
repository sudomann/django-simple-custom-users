=====
Django Simple Custom Users
=====

**Note:** Compatible with Postgres Only

django-simple-custom-users is a simple Pluggable custom user module for Django.

It provides a custom user model with the following attributes:
Required fields: 
- email (case insensitive for comparison, to avoid spoofing)
- password
- date-of-birth
- ...

Optional Fields:
- phone
- ...

More documentation will soon be available in the "docs" directory.

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


NOTE: Build with `python setup.py sdist`