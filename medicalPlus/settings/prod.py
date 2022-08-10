import os
from .common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['medicalplus-prod.herokuapp.com', 'zahrarhn.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': os.environ['DATABASE_ENGINE'],
        'NAME': os.environ['DATABASE_NAME'],
        'HOST': os.environ['DATABASE_HOST'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['DATABASE_PASSWORD']
    }
}