#!/usr/bin/env python

import os
import gettext
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

from controllers.admin_home import AdminHome
from controllers.admin_add_status import AdminAddStatus
from controllers.admin_add_severity import AdminAddSeverity

from controllers.admin_status_collection import AdminStatusCollection
from controllers.admin_status_resource import AdminStatusResource

from controllers.admin_severity_collection import AdminSeverityCollection
from controllers.admin_severity_resource import AdminSeverityResource

def main():
	application = webapp.WSGIApplication([
										('/admin/', AdminHome),

										(r'/admin/statuses', AdminStatusCollection),
										(r'/admin/statuses\.(en|cs)', AdminStatusCollection),
										(r'/admin/statuses\.(en|cs)\.(json|html|xml)', AdminStatusCollection),
										(r'/admin/status/([0-9]+)', AdminStatusResource),
										(r'/admin/status/([0-9]+)\.(en|cs)', AdminStatusResource),
										(r'/admin/status/([0-9]+)\.(en|cs)\.(json|html|xml)', AdminStatusResource),

										(r'/admin/severities', AdminSeverityCollection),
										(r'/admin/severities\.(en|cs)', AdminSeverityCollection),
										(r'/admin/severities\.(en|cs)\.(json|html|xml)', AdminSeverityCollection),
										(r'/admin/severity/([0-9]+)', AdminSeverityResource),
										(r'/admin/severity/([0-9]+)\.(en|cs)', AdminSeverityResource),
										(r'/admin/severity/([0-9]+)\.(en|cs)\.(json|html|xml)', AdminSeverityResource),

										], debug=True)
	run_wsgi_app(application)


if __name__ == '__main__':
	main()
