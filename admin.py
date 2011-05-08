#!/usr/bin/env python

import os
import gettext
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

from controllers.admin_home import AdminHome
from controllers.admin_list_severities import AdminListSeverities
from controllers.admin_list_statuses import AdminListStatuses
from controllers.admin_add_status import AdminAddStatus
from controllers.admin_add_severity import AdminAddSeverity

os.environ['DJANGO_SETTINGS_MODULE'] = 'config'
from django.conf import settings

settings._target = None

def main():
	application = webapp.WSGIApplication([
										('/admin/', AdminHome),

										('/admin/list-statuses', AdminListStatuses),
										('/admin/list-statuses.(en|cs)', AdminListStatuses),
										('/admin/list-statuses.(en|cs)\.(json|html|xml)', AdminListStatuses),

										('/admin/list-severities', AdminListSeverities),

										('/admin/add-status', AdminAddStatus),
										('/admin/add-severity', AdminAddSeverity),

										], debug=True)
	run_wsgi_app(application)


if __name__ == '__main__':
	main()
