#!/usr/bin/env python

from google.appengine.dist import use_library
use_library('django', '1.2')

import config
from django.conf import settings


settingsKeys = filter(lambda name: str(name) == str(name).upper(), dir(config))

settingsDict = {}
for key in settingsKeys:
	settingsDict[key] = getattr(config, key)

settings.configure(**settingsDict)
