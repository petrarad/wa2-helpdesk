#!/usr/bin/env python

import os
from django.utils import simplejson as json
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import login_required
from google.appengine.api import users
from google.appengine.ext.webapp import template
from google.appengine.api import mail

import config
from controllers.base import Base
from controllers.ticket_base import TicketBase
from models.ticket_service import TicketService
from models.status_service import StatusService
from models.severity_service import SeverityService
from models.comment_service import CommentService

HOST_NAME = 'wa2-helpdesk.appspot.com'

class ViewTicket(TicketBase):
	@login_required
	def get(self, ticketId, lang = 'en', output = 'html'):
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
		ticket = TicketService.getById(ticketId)

		ticketDict = {
			'id': ticket.key().id(),
			'project': ticket.project,
			'url': '/ticket/%d' % ticket.key().id(),
			'summary': ticket.summary,
			'description': ticket.description,
			'status': ticket.status.name,
			'severity': ticket.severity.name,
			'owner': ticket.author.nickname(),
			'solver': ticket.assignedUser.nickname() if ticket.assignedUser else '-',
			'solverEmail': ticket.assignedUser.email() if ticket.assignedUser else ''
		}

		statuses = [ {
			'id': s.key().id(),
			'name': s.name,
		} for s in StatusService.getAll() ]

		severities = [ {
			'id': s.key().id(),
			'name': s.name,
		} for s in SeverityService.getAll() ]

		comments = [ {
			'author': c.author.nickname(),
			'message': c.message,
			'date': c.date,
		} for c in CommentService.getByTicket(ticketId) ]

		contacts = self.GetContacts()
		if ticket.assignedUser:
			userEmail = ticket.assignedUser.email()
			index = [k for k, v in contacts.iteritems() if v == userEmail]
			if len(index):
				del contacts[index[0]]
				contacts['%s (now assigned)' % index[0]] = userEmail
			else:
				assignedUserName = '%s - %s (now assigned)' % (ticket.assignedUser.nickname(), userEmail)
				contacts[assignedUserName] = userEmail

		self.values['ticket'] = ticketDict
		self.values['statuses']   = statuses
		self.values['severities'] = severities
		self.values['comments'] = comments
		self.values['contacts'] = contacts

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

		self.current_user = users.GetCurrentUser()
		
		if not self.current_user:
			return self.toLogin()
		else:
			self.token = self.request.get('token')
			self.ManageAuth()
			self.LookupToken()

			if self.client.GetAuthSubToken() is None:
				return self.toAuthorize()

		ticket.author = user
		ticket.status = StatusService.getById(self.request.get('status'))
		ticket.severity = SeverityService.getById(self.request.get('severity'))
		ticket.summary = self.request.get('summary')
		ticket.description = self.request.get('description')
		if self.request.get('assignedUser'):
			if(ticket.assignedUser):
				if( ticket.assignedUser.email() != self.request.get('assignedUser') ):
					taskUrl = "%s/ticket/%s" % ('http://%s' % HOST_NAME, ticketId)
					mail.send_mail(
					sender= user.email(),
					to= self.request.get('assignedUser'),
					subject="Task assigned",
					body="""
%s  assigned you task %s

link: %s
""" % (user.nickname(),ticket.summary,taskUrl))
			ticket.assignedUser = users.User(self.request.get('assignedUser'))
		ticket.put()
		self.redirect('/ticket/%d' % ticket.key().id())
