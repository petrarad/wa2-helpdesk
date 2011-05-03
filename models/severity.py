#!/usr/bin/env python

from google.appengine.ext import db

class Severity(db.Model):
	name = db.StringProperty(multiline=False)
