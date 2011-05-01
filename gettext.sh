#!/bin/bash


export PYTHONPATH=../lib/django_1_2/
python2 ../lib/django_1_2/django/bin/django-admin.py makemessages -l cs_CZ
python2 ../lib/django_1_2/django/bin/django-admin.py makemessages -l en
