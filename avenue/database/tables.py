# Copyricht (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Defines the tables used by the database.
'''

from sqlalchemy import Table, Integer, ForeignKey, DateTime, Column, String, Boolean

def get_tables(metadata):
    table = {}

    def create_table(name, *columns):
        table[name] = Table(name, metadata,
                            Column('id', Integer, primary_key=True),
                            *columns)

    # TODO: posts, threads, users, urls, navbar, tags, styles
    # TODO: Work a per-forum karma system.

    # TODO: Work on a post revision system and a way to handle first
    # tags specially as content type.

    # TODO: Store parent/children/tags
    create_table('post',
                 Column('author', ForeignKey('user.username')),
                 Column('karma', Integer),
                 Column('content', String),
                 Column('date', DateTime),
                 Column('parent', ForeignKey('post.id')))

    # TODO: Store tags/threaded/author... read it from 'start' post.
    create_table('thread',
                 Column('start', ForeignKey('post.id')),
                 Column('title', String))

    create_table('user',
                 Column('username', String, unique=True),
                 Column('joined', DateTime),
                 Column('email', String))

    create_table('url_redirect',
                 Column('url', String),
                 Column('action', String))

    create_table('nav',
                 Column('visible', Boolean),
                 Column('title', String),
                 Column('text', String),
                 Column('link', String))

    create_table('tag',
                 Column('text', String),
                 Column('color', String))

    create_table('forum',
                 Column('name', String),
                 Column('url', String))

    create_table('theme_text',
                 Column('name', String, unique=True),
                 Column('plain', String),
                 Column('link', String),
                 Column('hover', String),
                 Column('heading', String),
                 Column('head_hover', String),
                 Column('nav', String),
                 Column('nav_hover', String))

    create_table('theme_background',
                 Column('name', String, unique=True),
                 Column('plain', String),
                 Column('article', String),
                 Column('post_1', String),
                 Column('post_2', String),
                 Column('box1', String),
                 Column('box2', String))

    create_table('theme_post',
                 Column('name', String, unique=True),
                 Column('level0', String),
                 Column('level1', String),
                 Column('level2', String),
                 Column('level3', String),
                 Column('level4', String),
                 Column('level5', String))

    create_table('theme',
                 Column('name', String, unique=True),
                 Column('url', String, unique=True),
                 Column('text', ForeignKey('theme_text.name')),
                 Column('background', ForeignKey('theme_background.name')),
                 Column('post', ForeignKey('theme_post.name')))

    return table
