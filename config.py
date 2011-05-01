#!/usr/bin/env python

import os

templateDir = os.path.join(os.path.dirname(__file__), 'templates')

USE_I18N = True

LANGUAGES = (
    ('en', _('English')),
    ('cs_CZ', _('Czech')),
)
