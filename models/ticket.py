#!/usr/bin/env python

from google.appengine.ext import db

from status import Status
from severity import Severity

class Ticket(db.Model):
	author = db.UserProperty()
	assignedUser = db.UserProperty()
	project = db.StringProperty(multiline=False)
	severity = db.ReferenceProperty(Severity)
	status = db.ReferenceProperty(Status)
	summary = db.StringProperty(multiline=False)
	description = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)
