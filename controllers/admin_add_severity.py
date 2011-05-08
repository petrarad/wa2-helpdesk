#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.api import users

from models.severity import Severity
from controllers.base import Base

class AdminAddSeverity(Base):

	def post(self):
		severity = Severity()

		user = users.get_current_user()
		if not user:
			self.redirect('/')

		severity.name = self.request.get('name')
		severity.put()
		self.redirect('/admin/')
