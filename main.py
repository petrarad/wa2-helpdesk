#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from controllers.list_tickets import ListTickets
from controllers.add_ticket import AddTicket

def main():
	application = webapp.WSGIApplication([
										('/', ListTickets),
										('/add-ticket', AddTicket)
										], debug=True)
	run_wsgi_app(application)


if __name__ == '__main__':
	main()
