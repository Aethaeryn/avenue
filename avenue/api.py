'''Currently, this is very messy code. Basically, you import this into
things that Avenue imports (e.g. Federation) so that they use the same
Flask instance as Avenue.
'''
from flask import json, make_response, render_template
from os import path
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
