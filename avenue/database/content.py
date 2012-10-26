# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Loads content into the database.
'''

from api import read_data
from database import table, connection

def import_data():
    data = read_data('forum')
    return data['style']


def insert_data():
    data = import_data()

    actions = []

    actions.append(table['text_theme'].insert().values(**data['night']['text']))
    actions.append(table['background_theme'].insert().values(**data['night']['background']))
    actions.append(table['post_theme'].insert().values(**data['night']['post']))

    for action in actions:
        connection.execute(action)

insert_data()
