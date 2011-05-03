#!/usr/bin/env python

import os
from django.utils import simplejson as json
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template

import config
from controllers.base import Base
from models.ticket_service import TicketService

class ViewTicket(Base):

	def get(self, ticketId, lang = 'en', output = 'html'):
		self.setLanguage(lang)

		ticket = TicketService.getById(ticketId)

		ticket = {
			'id': ticket.key().id(),
			'url': '/ticket/%d' % ticket.key().id(),
			'summary': ticket.summary,
			'description': ticket.description,
			'owner': ticket.author.nickname(),
		}

		self.values['ticket'] = ticket

		if output == 'html':
			self.render('ticket_detail.html')
		if output == 'xml':
			self.render('ticket_detail.xml')
		elif output == 'json':
			json.dump(ticket, self.response.out, indent = 4)

	def post(self, ticketId, lang = 'en', output = 'html'):
		ticket = TicketService.getById(ticketId)

		user = users.get_current_user()
		if not user:
			self.redirect('/')

		ticket.author = user

		ticket.summary = self.request.get('summary')
		ticket.description = self.request.get('description')
		ticket.put()
		self.redirect('/ticket/%d' % ticket.key().id())
