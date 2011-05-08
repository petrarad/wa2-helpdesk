#!/usr/bin/env python

from google.appengine.ext import db

from models.ticket import Ticket
from models.status import Status

class TicketService:

	@staticmethod
	def getAll(limit = 10):
		return db.GqlQuery("SELECT * FROM Ticket ORDER BY date DESC LIMIT %d" % limit)

	@staticmethod
	def getOpened(limit = 10):
		r = db.GqlQuery("SELECT __key__ FROM Status WHERE name = 'Closed' LIMIT 1")

		return db.GqlQuery("SELECT * FROM Ticket WHERE status != KEY('Status', %d) LIMIT %d" % (r.get().id(), limit))

	@staticmethod
	def getById(id):
		k = db.Key.from_path('Ticket', int(id))
		return Ticket.get(k)
