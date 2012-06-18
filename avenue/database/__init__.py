# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''This submodule manages the database.
'''

from sqlalchemy import create_engine, Table, MetaData, Integer, ForeignKey, DateTime, Column, String

LOCATION = 'sqlite:///:memory:'

engine = create_engine(LOCATION, echo=False)
metadata = MetaData()
metadata.create_all(engine)

# Store parent/children/revisions/tags/content-type
posts = Table('posts', metadata,
              Column('id', Integer, primary_key=True),
              Column('author', None, ForeignKey('users.username')),
              Column('karma', Integer),
              Column('content', String),
              Column('parent', None, ForeignKey('posts.id')))

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('username', String, unique=True),
              Column('joined', DateTime),
              Column('email', String),
              Column('karma', Integer))

connection = engine.connect()
