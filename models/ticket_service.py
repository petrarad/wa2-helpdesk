#!/usr/bin/env python

from google.appengine.ext import db

from models.ticket import Ticket

class TicketService:

	@staticmethod
	def getAll(limit = 10):
		return db.GqlQuery("SELECT * FROM Ticket ORDER BY date DESC LIMIT %d" % limit)

	@staticmethod
	def getById(id):
		k = db.Key.from_path('Ticket', int(id))
		return Ticket.get(k)
