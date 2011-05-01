#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import users


class MainHandler(webapp.RequestHandler):
    def get(self):
		user = users.get_current_user()

		if user:
			self.response.headers['Content-Type'] = 'text/html'
			self.response.out.write('WA2 Helpdesk!!' + user.nickname())
		else:
			self.redirect(users.create_login_url(self.request.uri))


def main():
	application = webapp.WSGIApplication([('/', MainHandler)], debug=True)
	run_wsgi_app(application)


if __name__ == '__main__':
	main()
