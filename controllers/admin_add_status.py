#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.api import users

from models.status import Status
from controllers.base import Base

class AdminAddStatus(Base):

	def post(self):
		status = Status()

		user = users.get_current_user()
		if not user:
			self.redirect('/')

		status.name = self.request.get('name')
		status.put()
		self.redirect('/admin/')
