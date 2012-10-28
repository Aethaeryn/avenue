# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Loads content into the database.
'''

from avenue.api import read_data
from avenue.database import table, connection

def import_data(filename):
    '''Imports data from a data file to be used in the database.
    '''
    data = read_data(filename)
    return data


def insert_data():
    '''Inserts static data from a data file into the database.
    '''
    data = import_data('themes')

    actions = []
    subtheme = set(['text', 'background', 'post'])

    for entry in data:
        entry_type = entry.pop('type')

        if entry_type in subtheme:
            actions.append(table['theme_%s' % entry_type].insert().values(**entry))

        else:
            actions.append(table['theme'].insert().values(**entry))

    for action in actions:
        connection.execute(action)

def get_theme():
    '''Retrieves a theme from the database.
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

    def read_database(name, first=False, search=False):
        '''Reads a table from a database and returns the keys and rows
        or row. If the list 'search' is defined, it looks for
        search[0] in the entry search[1]. Result is either one row or
        multiple rows, depending on if first is true or not.
        '''
        if search:
            sql = table[name].select().where('%s == "%s"' % (search[1], search[0]))
        else:
            sql = table[name].select()

        in_table = connection.execute(sql)

        keys = in_table.keys()

        if first:
            result = in_table.first()
        else:
            result = in_table.fetchall()

        in_table.close()

        return keys, result

    def theme_dict():
        '''Makes a dictionary of themes from a SQL table.
        '''
        themes = {}

        keys, rows = read_database('theme')

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

        if name:
            themes[name] = row_dict

        return themes

    def subtheme_dict(database, search):
        '''Makes a dictionary of subthemes (text, background, or post)
        from a SQL table.
        '''
        dictionary = {}

        keys, row = read_database(database, first=True, search=search)

        for i in range(len(keys)):
            dictionary[keys[i]] = row[i]

        return dictionary

    return theme_dict()
