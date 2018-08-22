#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

### THEME SETTINGS
THEME = 'attila'
# Theme customizations
HEADER_COVER = 'images/banner_biocomp.png'
HEADER_COLOR = 	'white'

COLOR_SCHEME_CSS = 'github.css'

CSS_OVERRIDE = ['theme/css/biocomp.css']
JS_OVERRIDE = []

# Author
AUTHOR_INTRO = u'Biocomp'
AUTHOR_DESCRIPTION = u'N\xfacleo de Pesquisa em Biodiversidade e Computa\xe7\xe3o'
AUTHOR_AVATAR = ''
AUTHOR_WEB = 'http://www.biocomp.life'

# Services
GOOGLE_ANALYTICS = ''
DISQUS_SITENAME = ''

# Social
SOCIAL = (
    ('github', 'https://github.com/BioComp-USP'),    
)

# Menu
MENUITEMS = (
    ('Sobre', '/categories.html' ),
    ('Pessoas', '/membros.html'),
    ('Projetos', '/projetos.html'),
    ('Publicações', '/publicacoes.html'),
    ('Oportunidades', '/oportunidades.html'),
)

###########################
### PLUGINS #####
PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = [
  'sitemap',
  'neighbors',
  'assets'
]

SITEMAP = {'format': 'xml'}

######################


#######################
AUTHOR = u'Biocomp'
SITENAME = u'N\xfacleo de Pesquisa em Biodiversidade e Computa\xe7\xe3o - Biocomp'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 0

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
