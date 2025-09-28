#!/usr/bin/env python
# -*- coding: utf-8 -*-

AUTHOR = 'Lucien Piat'
SITENAME = 'Lucien Piat Portfolio'
SITEURL = 'https://lucienpiat.fr'

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# IMPORTANT: Set the theme path
THEME = 'themes/under-construction'

# Disable feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Disable unnecessary pages for under construction
DIRECT_TEMPLATES = ['index']
PAGINATED_TEMPLATES = {
    'index': None,
    'tag': None,
    'category': None,
    'author': None,
}

# Disable pagination
DEFAULT_PAGINATION = False

# Static paths
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

# For local development
RELATIVE_URLS = True