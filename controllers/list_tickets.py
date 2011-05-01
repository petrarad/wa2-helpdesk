#!/usr/bin/env python

import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import login_required
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.api import users

import config

class ListTickets(webapp.RequestHandler):

	@login_required
	def get(self):
		user = users.get_current_user()

		tickets = db.GqlQuery("SELECT * FROM Ticket ORDER BY date DESC LIMIT 10")

		template_values = {
			'tickets': tickets
		}

		path = os.path.join(config.templateDir, 'index.html')
		self.response.out.write(template.render(path, template_values))
