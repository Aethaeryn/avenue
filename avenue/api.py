# Copyright (c) 2011, 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Currently, this is very messy code. Basically, you import this into
things that Avenue imports (e.g. Federation) so that they use the same
Flask instance as Avenue.
'''
from flask import json, request, make_response, render_template
from docutils.core import publish_parts
from os import path, listdir
import yaml

def read_data(filename):
    '''Reads in data from a given YML file and returns it in a form
    usable by Python.
    '''
    filename = '%s.yml' % filename

    data_file = open(path.join(path.dirname(__file__), 'data', filename))
    data = yaml.load(data_file)
    data_file.close()

    return data

def make_json(dictionary):
    '''Helper function that makes sure that the data served is
    recognized by browers as JSON.
    '''
    response = make_response(json.dumps(dictionary))
    response.mimetype = 'application/json'
    return response

def make_css(theme):
    '''Helper function that makes sure that the CSS served is
    recognized by browsers as CSS.
    '''
    response = make_response(render_template('main.css', theme=theme))
    response.mimetype = 'text/css'
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

def make_page(**kwargs):
    '''Used by plugins to Avenue, such as games, to generate a page
    integrated into the rest of the website.
    '''
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

def markup_to_html(string):
    '''Use docutils to turn the reStructuredText markup language into
    HTML that can be used elsewhere. Less than and greater than signs
    are properly escaped so the returned unicode string can be trusted
    in the HTML templates. Unicode is always returned, even if an
    ordinary string is passed in.
    '''
    #### TODO: The way headings are handled is currently not ideal and
    #### sometimes headings will need 'html_body' instead of 'body' to
    #### even show up here at all!
    return publish_parts(string, writer_name='html')['body']
