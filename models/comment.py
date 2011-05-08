#!/usr/bin/env python

from google.appengine.ext import db

from models.ticket import Ticket

class Comment(db.Model):
	author = db.UserProperty()
	ticket = db.ReferenceProperty(Ticket)
	message = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)
