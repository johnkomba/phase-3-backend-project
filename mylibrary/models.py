#!/usr/bin/env python3

from sqlalchemy import create_engine, desc
from sqlalchemy import (Column, Integer, String, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
engine = create_engine('sqlite:///mybooks.sqlite')

Base = declarative_base()
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Define the relationship between Author and Book
    books = relationship('Book', back_populates='author')
    
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

    # Define the relationship between Book and Author
    author = relationship('Author', back_populates='books')

    # Define the relationship between Book and Genre
    genre = relationship('Genre', back_populates='books')

    # Define the relationship between Book and Publisher
    publisher = relationship('Publisher', back_populates='books')
    
class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Define the relationship between Genre and Book
    books = relationship('Book', back_populates='genre')
    
class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    # Define the relationship between Publisher and Book
    books = relationship('Book', back_populates='publisher')

    