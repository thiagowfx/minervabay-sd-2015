# -*- coding: utf-8 -*-

from . import (Session, Book)

def par(s):
    return '%' + s + '%'

def add_book_to_database(book):
    title = book["title"]
    author = book["author"]
    publisher = book["publisher"]
    category = book["category"]
    isbn = book["isbn"]

    book_instance = Book(title = title, author = author, publisher = publisher, category = category, isbn = isbn)

    session = Session()
    session.add(book_instance)
    session.commit()

    return True

def search_book_in_database(query):
    search_string = query["search_string"]
    search_criteria = query["search_criteria"]

    session = Session()
    results = session.query(Book).filter(getattr(Book, search_criteria).like(par(search_string))).all()

    books = []
    for entry in results:
        books.append(entry.to_dict())

    json_response = {"data": books}
    return json_response
