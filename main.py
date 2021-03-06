#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bootstrap
import os
import gettext
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

from controllers.list_tickets import ListTickets
from controllers.add_ticket import AddTicket
from controllers.view_ticket import ViewTicket
from controllers.add_comment import AddComment

def main():
	application = webapp.WSGIApplication([
										('/(|all|opened)', ListTickets),
										('/(all|opened)\.(en|cs)', ListTickets),
										('/(all|opened)\.(en|cs)\.(json|html|xml)', ListTickets),

										(r'/add-ticket', AddTicket),

										(r'/ticket/([0-9]+)', ViewTicket),
										(r'/ticket/([0-9]+)\.(en|cs)', ViewTicket),
										(r'/ticket/([0-9]+)\.(en|cs)\.(json|html|xml)', ViewTicket),

										(r'/ticket/([0-9]+)/add-comment', AddComment),

										], debug=True)
	run_wsgi_app(application)


if __name__ == '__main__':
	main()
