#!/usr/bin/env python

from google.appengine.ext import db

from models.comment import Comment
from models.ticket import Ticket

class CommentService:

	@staticmethod
	def getAll(limit = 10):
		return db.GqlQuery("SELECT * FROM Comment ORDER BY date ASC LIMIT %d" % limit)

	@staticmethod
	def getById(id):
		k = db.Key.from_path('Comment', int(id))
		return Ticket.get(k)

	@staticmethod
	def getByTicket(ticketId):
		return db.GqlQuery("SELECT * FROM Comment WHERE ticket = KEY('Ticket', %d) ORDER BY date ASC" % int(ticketId))
