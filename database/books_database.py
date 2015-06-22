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
    magnetlink = book["magnetlink"]

    book_instance = Book(title = title, author = author, publisher = publisher, category = category, isbn = isbn, magnetlink = magnetlink)

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

def delete_book_from_database(book):
    id = book["id"]

    session = Session()
    book1 = session.query(Book).filter_by(id=id).first()
    session.delete(book1)
    session.commit()

    return True
