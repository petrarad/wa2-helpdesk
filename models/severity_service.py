#!/usr/bin/env python

from google.appengine.ext import db

from models.severity import Severity

class SeverityService:

	@staticmethod
	def getAll(limit = 10):
		return db.GqlQuery("SELECT * FROM Severity ORDER BY name ASC LIMIT %d" % limit)

	@staticmethod
	def getById(id):
		k = db.Key.from_path('Severity', int(id))
		return Severity.get(k)
