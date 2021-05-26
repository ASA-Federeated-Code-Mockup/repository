#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os

AUTHOR = 'admin'
SITENAME = 'SLRB'
SITEURL = ''


PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
DISPLAY_PAGES_ON_MENU = True

#THEME = os.path.join(os.getcwd(), 'slrbtheme')
#THEME = 'simple'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Plugins
# PLUGINS = [
            # 'minchin.pelican.plugins.cname',
          # ]

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),
        )
# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True