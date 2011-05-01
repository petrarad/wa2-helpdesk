#!/usr/bin/env python

import cgi
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.api import users

from ticket import Ticket

class MainHandler(webapp.RequestHandler):
    def get(self):
		user = users.get_current_user()

		if user:
			self.response.headers['Content-Type'] = 'text/html'
			self.response.out.write('<html><body>')

			tickets = db.GqlQuery("SELECT * FROM Ticket ORDER BY date DESC LIMIT 10")

			template_values = {
				'tickets': tickets
			}

			path = os.path.join(os.path.dirname(__file__), 'index.html')
			self.response.out.write(template.render(path, template_values))
		else:
			self.redirect(users.create_login_url(self.request.uri))

class AddTicket(webapp.RequestHandler):
	def post(self):
		ticket = Ticket()

		user = users.get_current_user()
		if not user:
			self.redirect('/')

		ticket.author = user

		ticket.description = self.request.get('description')
		ticket.put()
		self.redirect('/')

def main():
	application = webapp.WSGIApplication([
										('/', MainHandler),
										('/add-ticket', AddTicket)
										], debug=True)
	run_wsgi_app(application)


if __name__ == '__main__':
	main()
