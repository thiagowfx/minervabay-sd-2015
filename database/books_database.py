# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String
from . import (Base, engine, Session)

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publisher = Column(String)
    category = Column(String)
    isbn = Column(String)

    def __repr__(self):
        return "<Book(title='%s', author='%s', publisher='%s', category='%s', isbn='%s')>" % (self.title, self.author, self.publisher, self.category, self.isbn)


def add_book_to_database(book):
    title = book["title"]
    author = book["author"]
    publisher = book["publisher"]
    category = book["autocomplete"]
    isbn = book["isbn"]

    book_instance = Book(title = title, author = author, publisher = publisher, category = category, isbn = isbn)

    Base.metadata.create_all(engine)
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
