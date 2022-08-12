import os
from .common import *

DEBUG = False

SECRET_KEY = '(^!6ez)&2y1k$psy_9*#4@w=@s+j0b*6ant&xs4_!l(n5+=*0y'

ALLOWED_HOSTS = ['86.106.142.102', 'server1.medicalPlus.com', 'medicalplus-prod.herokuapp.com', 'zahrarhn.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'medicalPlusDB',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '6052re%Ol',
	'PORT': '',

       	'CHARSET': 'utf8',

       	'COLLATION': 'utf8_general_ci',
    }
}
