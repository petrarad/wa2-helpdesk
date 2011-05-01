#!/usr/bin/env python

import os
import gettext
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from controllers.list_tickets import ListTickets
from controllers.add_ticket import AddTicket
from google.appengine.ext.webapp import template

os.environ['DJANGO_SETTINGS_MODULE'] = 'config'
from django.conf import settings

settings._target = None

def main():
	application = webapp.WSGIApplication([
										('/', ListTickets),
										('/add-ticket', AddTicket)
										], debug=True)
	run_wsgi_app(application)


if __name__ == '__main__':
	main()
