import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-simple-custom-users',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-countries>=5.3.3,<6.0',
        'django-phonenumber-field>=3.0.1,<4.0',
        'phonenumbers>=8.10.13,<9.0',
        'psycopg2>=2.8.4,<3.0',
        'pyuca>=1.2,<2.0',  # Provides more accurate sorting of translated country names
    ],
    license='Apache 2.0 License',
    description='A simple Django app that provides a custom user model.',
    long_description=README,
    url='https://github.com/sudomann/django-simple-custom-users',
    author='Willy Njundong',
    author_email='njunongw@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache 2.0 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
