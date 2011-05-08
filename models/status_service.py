#!/usr/bin/env python

from google.appengine.ext import db

from models.status import Status

class StatusService:

	@staticmethod
	def getAll(limit = 10):
		return db.GqlQuery("SELECT * FROM Status ORDER BY name ASC LIMIT %d" % limit)

	@staticmethod
	def getById(id):
		k = db.Key.from_path('Status', int(id))
		return Status.get(k)
