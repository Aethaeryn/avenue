# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Loads content into the database.
'''

from avenue.api import read_data
from avenue.database import table, connection

def import_data():
    '''Imports data from a data file to be used in the database.
    '''
    data = read_data('forum')
    return data['style']


def insert_data():
    '''Inserts static data from a data file into the database.
    '''
    data = import_data()

    actions = []

    actions.append(table['theme_text'].insert().values(**data['night']['text']))
    actions.append(table['theme_background'].insert().values(**data['night']['background']))
    actions.append(table['theme_post'].insert().values(**data['night']['post']))
    actions.append(table['theme'].insert().values(name='night', text=1, post=1, background=1))

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
        or row. If first is true, it only returns the first match. If
        the list 'search' is defined, it looks for search[0] in the
        entry search[1]. Result is either one row or multiple rows,
        depending on if first is true or not.
        '''
        if search:
            sql = table[name].select().where('%s == %i' % (search[1], search[0]))
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

    def make_dict():
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
                    row_dict[keys[i]] = make_dict2(query[1][0], (query[0], query[1][1]))

                elif keys[i] == 'name':
                    name = row[i]

        if name:
            themes[name] = row_dict

        return themes

    def make_dict2(database, search):
        '''Makes a dictionary of themes from a SQL table.
        '''
        dictionary = {}

        keys, row = read_database(database, first=True, search=search)

        for i in range(len(keys)):
            dictionary[keys[i]] = row[i]

        return dictionary

    print make_dict()

insert_data()
get_theme()
