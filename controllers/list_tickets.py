#!/usr/bin/env python

import os
from django.utils import simplejson as json
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import login_required
from google.appengine.ext.webapp import template
from google.appengine.api import users

import config
from controllers.base import Base
from models.ticket_service import TicketService

class ListTickets(Base):

	@login_required
	def get(self, lang = '', output = 'html'):
		self.setLanguage(lang)
		user = users.get_current_user()

		tickets = [ {
			'id': t.key().id(),
			'url': '/ticket/%d' % t.key().id(),
			'description': t.description,
			'owner': t.author.nickname(),
		} for t in TicketService.getAll() ]

		template_values = {
			'tickets': tickets,
		}

		if output == 'html':
			path = os.path.join(config.templateDir, 'ticket_list.html')
			self.response.out.write(template.render(path, template_values))
		if output == 'xml':
			path = os.path.join(config.templateDir, 'ticket_list.xml')
			self.response.out.write(template.render(path, template_values))
		elif output == 'json':
			json.dump(tickets, self.response.out, indent = 4)

