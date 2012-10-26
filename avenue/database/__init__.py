# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''This submodule manages the database.
'''

from sqlalchemy import create_engine, MetaData
from avenue.database.tables import get_tables

# LOCATION = 'sqlite:///:memory:'
LOCATION = 'sqlite:////home/mbabich/foo.sqlite'

engine = create_engine(LOCATION, echo=True)
metadata = MetaData()
table = get_tables(metadata)
metadata.create_all(engine)
connection = engine.connect()
