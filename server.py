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

print "Starting CherryPy server..."
cherrypy.quickstart(Root(), '/', config = config)
