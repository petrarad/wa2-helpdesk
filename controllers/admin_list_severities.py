#!/usr/bin/env python

import os
from django.utils import simplejson as json
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import login_required
from google.appengine.api import users

import config
from controllers.base import Base
from models.severity_service import SeverityService

class AdminListSeverities(Base):

	@login_required
	def get(self, lang = '', output = 'html'):
		self.setLanguage(lang)

		severities = [ {
			'id': s.key().id(),
			'url': '/admin/severity/%d' % s.key().id(),
			'name': s.name,
		} for s in SeverityService.getAll() ]

		self.values['severities'] = severities

		if output == 'html':
			self.render('admin_severity_list.html')
		if output == 'xml':
			self.render('admin_severity_list.xml')
		elif output == 'json':
			json.dump(severities, self.response.out, indent = 4)

