#!/usr/bin/env python

from google.appengine.ext import db

from ticket_state import TicketState
from ticket_severity import TicketSeverity

class Ticket(db.Model):
	author = db.UserProperty()
	project = db.StringProperty(multiline=False)
	severity = TicketSeverity()
	state = TicketState()
	summary = db.StringProperty(multiline=False)
	description = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)
