#!/usr/bin/env python

import os
from django.utils import simplejson as json
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import login_required
from google.appengine.api import users

import config
from controllers.base import Base
from models.status_service import StatusService

class AdminListStatuses(Base):

	@login_required
	def get(self, lang = '', output = 'html'):
		self.setLanguage(lang)

		statuses = [ {
			'id': s.key().id(),
			'url': '/admin/status/%d' % s.key().id(),
			'name': s.name,
		} for s in StatusService.getAll() ]

		self.values['statuses'] = statuses

		if output == 'html':
			self.render('admin_status_list.html')
		if output == 'xml':
			self.render('admin_status_list.xml')
		elif output == 'json':
			json.dump(statuses, self.response.out, indent = 4)

