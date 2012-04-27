# Copyright (c) 2011, 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Currently, this is very messy code. Basically, you import this into
things that Avenue imports (e.g. Federation) so that they use the same
Flask instance as Avenue.
'''
from flask import json, request, make_response, render_template
from os import path, listdir

def make_json(dictionary):
    '''Helper function that makes sure that the data served is
    recognized by browers as JSON.
    '''
    response = make_response(json.dumps(dictionary))
    response.mimetype = 'application/json'
    return response

def check_cookie():
    '''Checks the cookie for the appropriate user.

    If there's no cookie, then the user is None.
    '''
    cookie = request.cookies.get('username')

    if cookie == 'michael':
        return True

    else:
        return False

#### TODO: Themes: mobile/desktop, dark/light, pretty/useful/plain
def make_page(**kwargs):
    return render_template('basic.html', **kwargs)

def get_header():
    '''Gets the custom HTML from templates/header.html, if it exists.
    '''
    template_path = path.join(path.dirname(__file__), 'templates')
    templates     = listdir(template_path)

    if 'header.html' in templates:
        header = open(path.join(template_path, 'header.html'), 'r')
        text   = header.read()

        header.close()
        return text

    else:
        return ''
