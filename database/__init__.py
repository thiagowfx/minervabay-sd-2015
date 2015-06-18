# -*- coding: utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_FILE = 'database/books.db'

Base = declarative_base()
engine = create_engine('sqlite:///' + DATABASE_FILE, echo=True)
Session = sessionmaker(bind=engine)
