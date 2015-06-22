#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import cherrypy

import json
from pyjsonrpc.cp import CherryPyJsonRpc, rpcmethod
from database import books_database

PORT = 8080
WEB_DIR = 'client'

class SdFront(object):
    @cherrypy.expose
    def index(self):
        return open(os.path.join(WEB_DIR, 'index.html'))

class SdRpc(CherryPyJsonRpc):
    index = CherryPyJsonRpc.request_handler

    @rpcmethod
    def addBook(self, book):
        return books_database.add_book_to_database(book)

    @rpcmethod
    def searchBook(self, query):
        return books_database.search_book_in_database(query)

    @rpcmethod
    def deleteBook(self, book):
        return books_database.delete_book_from_database(book)


def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"

cherrypy.config.update({
    'server.socket_port': PORT,
    'tools.CORS.on': True
    })

config = {
        '/view': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(os.path.dirname(os.path.abspath(__file__)), WEB_DIR)
            },
        }

cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '8080')),})

print "Starting CherryPy server..."
cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
root = SdRpc()
root.view = SdFront()
cherrypy.quickstart(root, '/', config = config)
