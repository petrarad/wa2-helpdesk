#!/usr/bin/env python

from google.appengine.ext import db

class Ticket(db.Model):
	author = db.UserProperty()
	description = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)
