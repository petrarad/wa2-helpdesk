#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.api import users

from models.ticket import Ticket
from models.status_service import StatusService
from models.severity_service import SeverityService

from controllers.base import Base

class AddTicket(Base):

	def post(self):
		ticket = Ticket()

		user = users.get_current_user()
		if not user:
			self.redirect('/')

		ticket.author = user

		ticket.status = StatusService.getById(self.request.get('status'))
		ticket.severity = SeverityService.getById(self.request.get('severity'))
		if self.request.get('assignedUser'):
			ticket.assignedUser = users.User(self.request.get('assignedUser'))
		ticket.description = self.request.get('description')
		ticket.summary = self.request.get('summary')
		ticket.put()
		self.redirect('/')
