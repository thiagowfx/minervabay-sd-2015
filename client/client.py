#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cherrypy
import os

class Root(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

config = {
        '/': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.dirname(os.path.abspath(__file__))
            }
        }

print "Starting cherrypy server..."
cherrypy.quickstart(Root(), '/', config=config)
print "Cont"
