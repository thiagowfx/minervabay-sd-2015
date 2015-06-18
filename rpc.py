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

    # TODO: store those things in the database / ORM.
    # Return False if there is some error with the data.

    return True

def search_book_in_database(query):
    search_string = query["search_string"]

    books = []

    # TODO: process query and append matched results to books list

    books.append({
        "title": "t",
        "author": "a",
        "publisher": "p",
        "autocomplete": "c",
        "isbn": "i"
        })

    json_response = {"data": books}
    return json_response

class Root(CherryPyJsonRpc):

    @rpcmethod
    def addBook(self, book):
        return add_book_to_database(book)

    @rpcmethod
    def searchBook(self, query):
        return search_book_in_database(query)

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
