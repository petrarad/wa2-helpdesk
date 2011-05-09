#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from django.utils import simplejson as json
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import login_required
from google.appengine.api import users

from controllers.base import Base
from models.ticket_service import TicketService
from models.status_service import StatusService
from models.severity_service import SeverityService

class ListTickets(Base):

	@login_required
	def get(self, lang = '', output = 'html'):
		self.setLanguage(lang)

		tickets = [ {
			'id': t.key().id(),
			'url': '/ticket/%d' % t.key().id(),
			'summary': t.summary,
			'description': t.description,
			'status': t.status.name,
			'severity': t.severity.name,
			'owner': t.author.nickname(),
		} for t in TicketService.getOpened() ]

		statuses = [ {
			'id': s.key().id(),
			'name': s.name,
		} for s in StatusService.getAll() ]

		severities = [ {
			'id': s.key().id(),
			'name': s.name,
		} for s in SeverityService.getAll() ]

		self.values['tickets']    = tickets
		self.values['statuses']   = statuses
		self.values['severities'] = severities

		if output == 'html':
			self.render('ticket_list.html')
		if output == 'xml':
			self.render('ticket_list.xml')
		elif output == 'json':
			json.dump(tickets, self.response.out, indent = 4)

