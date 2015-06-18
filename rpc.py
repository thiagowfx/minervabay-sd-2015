#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cherrypy
import json
from pyjsonrpc.cp import CherryPyJsonRpc, rpcmethod

import database

PORT = 8081

class Root(CherryPyJsonRpc):

    @rpcmethod
    def addBook(self, book):
        return database.add_book_to_database(book)

    @rpcmethod
    def searchBook(self, query):
        return database.search_book_in_database(query)

    index = CherryPyJsonRpc.request_handler

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"

cherrypy.config.update({
    'server.socket_port': PORT,
    'tools.CORS.on': True
    })

print "Starting RPC server ..."
print "URL: http://localhost:" + str(PORT)
cherrypy.tools.CORS = cherrypy.Tool('before_handler', CORS)
cherrypy.quickstart(Root())
