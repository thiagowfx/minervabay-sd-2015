# -*- coding: utf-8 -*-

from . import (Session, Book)

def add_book_to_database(book):
    title = book["title"]
    author = book["author"]
    publisher = book["publisher"]
    category = book["autocomplete"]
    isbn = book["isbn"]

    book_instance = Book(title = title, author = author, publisher = publisher, category = category, isbn = isbn)

    session = Session()
    session.add(book_instance)
    session.commit()

    return True

def search_book_in_database(query):
    search_string = query["search_string"]
    search_criteria = query["search_criteria"]

    books = []

    # TODO: process query and append matched results to books list
    # Do accordingly to the below example:

    books.append({
        "title": "t",
        "author": "a",
        "publisher": "p",
        "autocomplete": "c",
        "isbn": "i"
        })

    json_response = {"data": books}
    return json_response
