#!/usr/bin/env python

import os
from google.appengine.ext import webapp
from django.utils import translation

import config

class Base(webapp.RequestHandler):

	def setLanguage(self, lang = ''):
		self.request.COOKIES = self.request.cookies
		self.request.META = os.environ

		language = translation.get_language_from_request(self.request)

		if lang:
			if lang == 'cs':
				language = 'cs_CZ'
			else:
				language = 'en'

		translation.activate(language)
		self.request.LANGUAGE_CODE = translation.get_language()

		self.response.headers['Content-Language'] = translation.get_language()
