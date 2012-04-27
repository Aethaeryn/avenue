# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Acts as an interface between what Flask serves and what goes on in
the rest of the application.
'''
from avenue import app, api

@app.route('/')
def index():
    '''Serves the main page of the website.
    '''
    words = 'Hello, world!'

    return api.make_page(style='static/dark-plain', body=words)
