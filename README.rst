=====
Django Simple Custom Users
=====

django-simple-custom-users is a simple Pluggable custom user module for Django.

It provides a custom user model which requires an email, password, and date-of-birth 
to create an account.
Username is disabled, and phone number is optional.

More documentation will soon be available in the "docs" directory.

Quick start
-----------

1. Add "django-simple-custom-users" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'users',
    ]

2. Add `AUTH_USER_MODEL = 'users.CustomUser'` to your `settings.py`

3. Run `python manage.py migrate` to create the user model.

And you are ready to use as you please!


NOTE: Build with `python setup.py sdist`