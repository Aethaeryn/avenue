# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''This submodule manages the database.
'''

from sqlalchemy import create_engine, MetaData
from avenue.database.tables import get_tables

LOCATION = 'sqlite:///:memory:'
#LOCATION = 'sqlite:////home/mbabich/foo.sqlite'

def start_engine(location):
    engine = create_engine(location, echo=True)
    metadata = MetaData()
    get_tables(metadata)
    metadata.create_all(engine)
    return engine.connect()

connection = start_engine(LOCATION)
