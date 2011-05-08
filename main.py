#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import gettext
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

from controllers.list_tickets import ListTickets
from controllers.add_ticket import AddTicket
from controllers.view_ticket import ViewTicket

os.environ['DJANGO_SETTINGS_MODULE'] = 'config'
from django.conf import settings

settings._target = None

def main():
	application = webapp.WSGIApplication([
										('/', ListTickets),
										('/index.(en|cs)', ListTickets),
										('/index.(en|cs)\.(json|html|xml)', ListTickets),

										(r'/add-ticket', AddTicket),

										(r'/ticket/([0-9]+)', ViewTicket),
										(r'/ticket/([0-9]+)\.(en|cs)', ViewTicket),
										(r'/ticket/([0-9]+)\.(en|cs)\.(json|html|xml)', ViewTicket),

										], debug=True)
	run_wsgi_app(application)


if __name__ == '__main__':
	main()
