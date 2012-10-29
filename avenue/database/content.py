# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Loads content into the database.
'''
from avenue.api import read_data
from avenue.database import table, connection

def insert_data():
    '''Inserts static data from a data file into the database.
    '''
    def themes():
        '''Inserts the themes from themes.yml into the database.
        '''
        data = read_data('themes')

        subtheme = set(['text', 'background', 'post'])

        for entry in data:
            entry_type = entry.pop('type')

            if entry_type in subtheme:
                actions.append(table['theme_%s' % entry_type].insert().values(**entry))

            else:
                actions.append(table['theme'].insert().values(**entry))

    def forum_import(subsection):
        '''Inserts data from a forum subsection into the database.
        '''
        data = forum_data[subsection]

        for entry in data:
            actions.append(table[subsection].insert().values(**entry))

    actions = []
    forum_data = read_data('forum')

    themes()
    forum_import('nav')
    forum_import('tag')
    forum_import('url_redirect')

    for action in actions:
        connection.execute(action)

def _read_database(name, first=False, search=False):
    '''Reads a table from a database and returns the keys and rows
    or row. If the list 'search' is defined, it looks for
    search[0] in the entry search[1]. Result is either one row or
    multiple rows, depending on if first is true or not.
    '''
    if search:
        condition = '%s == "%s"' % (search[1], search[0])
        sql = table[name].select().where(condition)

    else:
        sql = table[name].select()

    in_table = connection.execute(sql)
    keys = in_table.keys()
    result = in_table.first() if first else in_table.fetchall()

    in_table.close()

    return keys, result

def get_themes():
    '''Retrieves the themes from the database.
    '''
    def get_foreign(table_name):
        '''Retrieves the foreign key information for columns in a
        given table that have them.
        '''
        foreign = {}

        for column in table[table_name].get_children():
            fkeys = column.foreign_keys

            if len(fkeys) == 1:
                for fkey in fkeys:
                    foreign[column.name] = fkey._colspec

        return foreign

    def subtheme_dict(database, search):
        '''Makes a dictionary of subthemes (text, background, or post)
        from a SQL table.
        '''
        dictionary = {}

        keys, row = _read_database(database, first=True, search=search)

        for i in range(len(keys)):
            dictionary[keys[i]] = row[i]

        return dictionary

    def theme_dict():
        '''Makes a dictionary of themes from a SQL table.
        '''
        themes = {}
        keys, rows = _read_database('theme')
        foreign = get_foreign('theme')

        for row in rows:
            row_dict = {}
            name = False

            for i in range(len(keys)):
                if keys[i] in foreign:
                    query = (row[i], foreign[keys[i]].split('.'))
                    row_dict[keys[i]] = subtheme_dict(query[1][0], (query[0], query[1][1]))

                elif keys[i] == 'name':
                    name = row[i]

                elif keys[i] == 'url':
                    row_dict[keys[i]] = row[i]

            if name:
                themes[name] = row_dict

        return themes

    return theme_dict()

def get_nav():
    '''Retrives the nav from the database.
    '''
    keys, rows = _read_database('nav')

    nav = []

    for row in rows:
        dictionary = {}

        for i in range(len(keys)):
            dictionary[keys[i]] = row[i]

        nav.append(dictionary)

    return nav

def get_tags():
    '''Retrieves the tags from the database.
    '''
    keys, rows = _read_database('tag')

    tags = {}

    for row in rows:
        dictionary = {}

        for i in range(len(keys)):
            dictionary[keys[i]] = row[i]

        tags[dictionary['text']] = dictionary

    return tags

def get_urls():
    '''Retrieves the redirect urls from the database.
    '''
    keys, rows = _read_database('url_redirect')

    dictionary = {}

    for row in rows:
        dictionary[row[1]] = row[2]

    return dictionary
