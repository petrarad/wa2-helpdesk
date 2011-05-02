#!/usr/bin/env python

from google.appengine.ext import db

class TicketState(db.Model):
	name = db.Key()
