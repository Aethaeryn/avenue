# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Acts as an interface between what Flask serves and what goes on in
the rest of the application.
'''
from avenue import app
from flask import render_template

@app.route('/')
def index():
    '''Serves the main page of the website.
    '''
    words = 'Hello, world!'

    #### TODO: Themes: mobile/desktop, dark/light, pretty/useful/plain
    return render_template('basic.html', style='dark-plain', body=words)
