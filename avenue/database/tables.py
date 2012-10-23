# Copyricht (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Defines the tables used by the database.
'''

from sqlalchemy import Table, Integer, ForeignKey, DateTime, Column, String, Boolean

def get_tables(metadata):
    table = {}

    def add_table(name, *columns):
        table[name] = Table(name, metadata,
                            Column('id', Integer, primary_key=True),
                            *columns)

    # TODO: posts, threads, users, urls, navbar, tags, styles
    # TODO: Work a per-forum karma system.

    # TODO: Work on a post revision system and a way to handle first
    # tags specially as content type.

    # TODO: Store parent/children/tags
    add_table('posts',
              Column('author', ForeignKey('users.username')),
              Column('karma', Integer),
              Column('content', String),
              Column('date', DateTime),
              Column('parent', ForeignKey('posts.id')))

    # TODO: Store tags/threaded/author... read it from 'start' post.
    add_table('thread',
              Column('start', ForeignKey('posts.id')),
              Column('title', String))

    add_table('users',
              Column('username', String, unique=True),
              Column('joined', DateTime),
              Column('email', String))

    add_table('nav',
              Column('visible', Boolean),
              Column('title', String),
              Column('text', String),
              Column('link', String))

    add_table('tags',
              Column('text', String),
              Column('color', String))

    add_table('forums',
              Column('name', String),
              Column('url', String))

    return table
