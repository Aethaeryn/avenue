'''The avenue package contains everything that is necessary to run an
Avenue server.

It utilizes a SQL database using SQLAlchemy. It then presents public
data via Flask and WSGI. It provides web pages under multiple
different themes and a JSON API for external applications to access.
'''
from flask import Flask

app = Flask(__name__)

from avenue import web

web.url_generator()

#import federation
#app.register_blueprint(federation.app)
