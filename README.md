# Django start point configuration

django with Custom User Model AbstractBaseUser class and Django-Allauth

####


## Getting started

## Setup

Follow these instructions to try this demo out locally.
I'm using pipenv, you can use pip instead for the virtual environment and install.

```bash

Pipenv Install requirements.txt in a new virtual environment
pipenv shell
django-admin startproject myweb .
pypenv manage.py startapp users
setting.py for users
setting.py for allauth
python manage.py migrate
python manage.py createsuperuser
