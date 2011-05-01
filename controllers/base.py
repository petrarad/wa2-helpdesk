#!/usr/bin/env python

import os
from google.appengine.ext import webapp
from django.utils import translation

class Base(webapp.RequestHandler):

	def initialize(self, request, response):
		webapp.RequestHandler.initialize(self, request, response)

		self.request.COOKIES = self.request.cookies #Cookies(self)
		self.request.META = os.environ

		language = translation.get_language_from_request(self.request)

		if self.request.get('lang'):
			if self.request.get('lang') == 'cs':
				language = 'cs_CZ'
			else:
				language = 'en'

		translation.activate(language)
		self.request.LANGUAGE_CODE = translation.get_language()

		self.response.headers['Content-Language'] = translation.get_language()
