#!/usr/bin/env python

from google.appengine.ext import db

class TicketSeverity(db.Model):
	name = db.StringProperty(multiline=False)
