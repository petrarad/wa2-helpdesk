#!/usr/bin/env python

from google.appengine.ext import db

from models.ticket import Ticket
from models.status import Status

class TicketService:

	@staticmethod
	def getAll(limit = 10, order = 'date', orderdir = 'desc'):
		if order == 'id':
			order = '__key__'
		if order not in ['date','summary', 'status', 'severity', '__key__','author','assignedUser']:
			order = 'date'
		
		return db.GqlQuery("SELECT * FROM Ticket ORDER BY %s %s LIMIT %d" % (order,orderdir.upper(),limit))

	@staticmethod
	def getOpened(limit = 10, order = 'id', orderdir = 'desc'):
		r = db.GqlQuery("SELECT __key__ FROM Status WHERE name = 'Closed' LIMIT 1")

		return db.GqlQuery("SELECT * FROM Ticket WHERE status != KEY('Status', %d) LIMIT %d" % (r.get().id(), limit))

	@staticmethod
	def getById(id):
		k = db.Key.from_path('Ticket', int(id))
		return Ticket.get(k)

	@staticmethod
	def getByStatus(status = '', limit = 10, order = 'date', orderdir = 'desc'):
		if(status == 'all'):
			return TicketService.getAll(limit, order, orderdir)
		else:
			return TicketService.getOpened(limit, order, orderdir)