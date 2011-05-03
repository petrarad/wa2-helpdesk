#!/usr/bin/env python

import os
import gettext
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

from controllers.admin_home import AdminHome

os.environ['DJANGO_SETTINGS_MODULE'] = 'config'
from django.conf import settings

settings._target = None

def main():
	application = webapp.WSGIApplication([
										('/admin/', AdminHome),

										], debug=True)
	run_wsgi_app(application)


if __name__ == '__main__':
	main()
