# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_FILE = 'database/books.db'

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publisher = Column(String)
    category = Column(String)
    isbn = Column(String)
    magnetlink = Column(String)

    def to_dict(self):
        return {
                "id": self.id,
                "title": self.title,
                "author": self.author,
                "publisher": self.publisher,
                "category": self.category,
                "isbn": self.isbn,
                "magnetlink": self.magnetlink
                }

    def __repr__(self):
        return "<Book(id='%d',title='%s', author='%s', publisher='%s', category='%s', isbn='%s', magnetlink='%s')>" % (self.id, self.title, self.author, self.publisher, self.category, self.isbn, self.magnetlink)

engine = create_engine('sqlite:///' + DATABASE_FILE, echo=True)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
