#!/usr/bin/env python

import os
from django.utils import simplejson as json
from google.appengine.ext import webapp
from google.appengine.api import users

from controllers.base import Base
from models.ticket_service import TicketService

class AdminHome(Base):

	def get(self, lang = 'en', output = 'html'):
		self.setLanguage(lang)
		self.values['show_admin_link'] = False


		if output == 'html':
			self.render('admin_home.html')
		if output == 'xml':
			self.render('admin_home.xml')
		elif output == 'json':
			json.dump(ticket, self.response.out, indent = 4)
