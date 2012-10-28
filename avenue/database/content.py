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

    # This executes a join. Not ideal for the data structure we want because the keys aren't a set (i.e. some titles are duplicates).
    print connection.execute(table['theme'].join(table['theme_post']).join(table['theme_background']).join(table['theme_text']).select()).keys()

    # This is just the table itself.
    print connection.execute(table['theme'].select())

    # These are the foreign columns.
    print get_foreign('theme')

insert_data()
get_theme()
