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

    themes = connection.execute(table['theme'].select())
    keys = themes.keys()
    rows = themes.fetchall()
    themes.close()
    foreign = get_foreign('theme')

    themes_dict = {}

    for row in rows:
        row_dict = {}

        for i in range(len(keys)):
            if keys[i] in foreign:
                print keys[i], row[i], foreign[keys[i]]

            else:
                row_dict[keys[i]] = row[i]

        print row_dict

insert_data()
get_theme()
