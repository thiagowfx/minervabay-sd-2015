#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cherrypy
import os

class Root(object):
    @cherrypy.expose
    def index(self):
        return open('cadastro.html')

if '__name__' == '__main__':

    conf = {
            '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': os.path.dirname(os.path.abspath(__file__))
                }
            }
    cherrypy.quickstart(Root(), '/', config=conf)
