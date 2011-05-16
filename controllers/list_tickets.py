#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import atom

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

import gdata.alt.appengine
import gdata.contacts.service
import gdata.service

from django.utils import simplejson as json
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import login_required
from google.appengine.api import users

from controllers.base import Base
from controllers.ticket_base import TicketBase
from models.ticket_service import TicketService
from models.ticket import Ticket
from models.status_service import StatusService
from models.severity_service import SeverityService
from models.stored_token import StoredToken

APP_INFO = """Info"""
APP_NAME = 'WA2 - Helpdesk'
HOST_NAME = 'wa2-helpdesk.appspot.com'

class ListTickets(TicketBase):
	@login_required
	def get(self, status = '', lang = '', output = 'html'):
		self.setLanguage(lang)
		self.current_user = users.GetCurrentUser()
		
		if not self.current_user:
			return self.toLogin()
		else:
			self.token = self.request.get('token')
			self.ManageAuth()
			self.LookupToken()
			
			if self.client.GetAuthSubToken() is None:
				return self.toAuthorize()
		
		tickets = [ {
			'id': t.key().id(),
			'url': '/ticket/%d' % t.key().id(),
			'project': t.project,
			'summary': t.summary,
			'description': t.description,
			'status': t.status.name,
			'severity': t.severity.name,
			'owner': t.author.nickname(),
			'solver': t.assignedUser.nickname() if t.assignedUser else '-'
		} for t in TicketService.getByStatus(status, 20, self.request.get('order'), self.request.get('orderdir')) ]

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
		self.values['contacts'] = self.GetContacts()

		if output == 'html':
			self.render('ticket_list.html')
		if output == 'xml':
			self.render('ticket_list.xml')
		elif output == 'json':
			json.dump(tickets, self.response.out, indent = 4)
	def post(self, status = '', lang = '', output = 'html'):
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
	def toAuthorize(self):
		self.values = {
			'authsub_url': self.client.GenerateAuthSubURL('http://%s/' % (HOST_NAME),'%s' % ('http://www.google.com/m8/feeds/'),secure=False, session=True),
			'app_name': APP_NAME,
		}
		return self.render('authorize_access.html')