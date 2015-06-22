#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import cherrypy

WEB_DIR = 'client'

class Root(object):
    @cherrypy.expose
    def index(self):
        return open(os.path.join(WEB_DIR, 'index.html'))

config = {
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(os.path.dirname(os.path.abspath(__file__)), WEB_DIR)
            }
        }

cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})

print "Starting Web server..."
cherrypy.quickstart(Root(), '/', config = config)
