#!/usr/bin/env python

import os
import json
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
			'description': ticket.description,
			'owner': ticket.author.nickname(),
		}

		template_values = {
			'ticket': ticket,
		}

		if output == 'html':
			path = os.path.join(config.templateDir, 'ticket_detail.html')
			self.response.out.write(template.render(path, template_values))
		if output == 'xml':
			path = os.path.join(config.templateDir, 'ticket_detail.xml')
			self.response.out.write(template.render(path, template_values))
		elif output == 'json':
			json.dump(ticket, self.response.out, indent = 4)
