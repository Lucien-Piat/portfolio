#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Basic Information
AUTHOR = 'Lucien Piat'
SITENAME = 'Lucien Piat'
SITESUBTITLE = 'Bioinformatician'
SITEDESCRIPTION = 'Lucien Piat - Bioinformatician | Bordeaux, France'
SITEURL = 'https://lucienpiat.fr'

PATH = 'content'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'en'

# Theme
THEME = 'themes/portfolio'

# Profile
PROFILE_IMAGE = 'images/profile.jpg'
AUTHOR_EMAIL = 'lucienpiat33@gmail.com'
AUTHOR_LOCATION = 'Bordeaux, France'

# Social Links
GITHUB_URL = 'https://github.com/Lucien-Piat'
LINKEDIN_URL = 'https://www.linkedin.com/in/lucien-piat-47930419b/'


# About Section
ABOUT_ME = """
TODO
"""

# Skills Section
SKILLS = {
    'A': ['TODO', 'TODO', 'TODO', 'TODO'],
    'B': ['TODO', 'TODO', 'TODO', 'TODO'],
    'C': ['TODO', 'TODO', 'TODO', 'TODO'],
}

# Projects Section
PROJECTS = [
    {
        'name': 'TODO',
        'description': 'TODO',
        'tech': ['TODO', 'TODO', 'TODO'],
        'github': 'TODO',
        'gitlab': 'TODO'
    }
]

# Static files
STATIC_PATHS = [
    'images',
    'extra/CNAME',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

# Disable feed generation
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Disable unnecessary page generation
DIRECT_TEMPLATES = ['index']
PAGINATED_TEMPLATES = {}

RELATIVE_URLS = True