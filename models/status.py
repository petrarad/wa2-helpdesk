#!/usr/bin/env python

from google.appengine.ext import db

class Status(db.Model):
	name = db.StringProperty(multiline=False)
