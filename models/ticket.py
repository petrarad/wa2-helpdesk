#!/usr/bin/env python

from google.appengine.ext import db

from status import Status
from severity import Severity

class Ticket(db.Model):
	author = db.UserProperty()
	project = db.StringProperty(multiline=False)
	severity = Severity()
	status = Status()
	summary = db.StringProperty(multiline=False)
	description = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)
