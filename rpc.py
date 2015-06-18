#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cherrypy
import json
from pyjsonrpc.cp import CherryPyJsonRpc, rpcmethod

PORT = 8081

def add_book_to_database(book):
    title = book["title"]
    author = book["author"]
    publisher = book["publisher"]
    category = book["autocomplete"]
    isbn = book["isbn"]

    # TODO: store those things in the database / ORM

    return True

class Root(CherryPyJsonRpc):

    @rpcmethod
    def addBook(self, book):
        return add_book_to_database(book)

    index = CherryPyJsonRpc.request_handler

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"

cherrypy.config.update({
    'server.socket_port': PORT,
    'tools.CORS.on': True
    })

print "Starting HTTP server ..."
print "URL: http://localhost:" + str(PORT)
cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
cherrypy.quickstart(Root())
