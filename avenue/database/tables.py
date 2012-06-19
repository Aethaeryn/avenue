# Copyricht (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Defines the tables used by the database.
'''

from sqlalchemy import Table, Integer, ForeignKey, DateTime, Column, String

def get_tables(metadata):
    table = {}

    # Store parent/children/revisions/tags/content-type
    table['posts'] = Table('posts', metadata,
                           Column('id', Integer, primary_key=True),
                           Column('author', ForeignKey('users.username')),
                           Column('karma', Integer),
                           Column('content', String),
                           Column('parent', ForeignKey('posts.id')))

    table['users'] = Table('users', metadata,
                           Column('id', Integer, primary_key=True),
                           Column('username', String, unique=True),
                           Column('joined', DateTime),
                           Column('email', String),
                           Column('karma', Integer))

    return table
