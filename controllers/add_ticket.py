#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.api import users

from models.ticket import Ticket

class AddTicket(webapp.RequestHandler):

	def post(self):
		ticket = Ticket()

		user = users.get_current_user()
		if not user:
			self.redirect('/')

		ticket.author = user

		ticket.description = self.request.get('description')
		ticket.put()
		self.redirect('/')