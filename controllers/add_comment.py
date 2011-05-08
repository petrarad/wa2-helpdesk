#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.api import users

from models.comment import Comment
from models.ticket_service import TicketService

from controllers.base import Base

class AddComment(Base):

	def post(self, ticketId):
		user = users.get_current_user()
		if not user:
			self.redirect('/')

		comment = Comment()

		ticket = TicketService.getById(ticketId)

		comment.author = user
		comment.ticket = ticket

		comment.message = self.request.get('message')
		comment.put()
		self.redirect('/ticket/' + ticketId)
