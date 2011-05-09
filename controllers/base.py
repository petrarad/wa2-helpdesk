#!/usr/bin/env python

import os
from google.appengine.ext import webapp
from django.utils import translation
from google.appengine.api import users
from google.appengine.ext.webapp import template

import config

class Base(webapp.RequestHandler):

	values = {}

	def initialize(self, request, response):
		webapp.RequestHandler.initialize(self, request, response)

		self.values['logout_link'] = users.create_logout_url('/')
		self.values['show_admin_link'] = users.is_current_user_admin()

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

	def render(self, templateFile):
		path = os.path.join(config.templateDir, templateFile)
		self.response.out.write(template.render(path, self.values))
