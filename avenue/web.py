# -*- coding: utf-8 -*-
# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Acts as an interface between what Flask serves and what goes on in
the rest of the application.
'''
from avenue import app, api
from flask import render_template, make_response
from copy import copy
import yaml
from os import path

heading = 'Zombie Raptor'
navbar = []
navbar.append({'title'    : 'Avenue',
               'content'  : 'Read about the Avenue platform that runs this website.',
               'link'     : '/about'})

navbar.append({'title'   : 'Federation',
               'content' : 'Form federations with your friends and plot to take over the galaxy!',
               'link'    : '/'})

navbar.append({'title'   : 'Zombie Raptor Blog',
               'content' : 'Read new updates from the Zombie Raptor team!',
               'link'    : '/'})

navbar.append({'title'   : 'Forums',
               'content' : 'Visit the official forums!',
               'link'    : '/f'})

browser_upgrade = '<p><img src="static/dl/firefox-g.png"></img><img src="static/dl/chrome-g.png"></img><img src="static/dl/safari-g.png"></img><img src="static/dl/opera-g.png"></img></p>'

def button(text):
    return '<div class="button">%s</div>' % text

buttons = '<p>%s%s%s%s&nbsp</p>' % (button(u'↳'), button('+'), button('-'), button('#'))

@app.route('/')
def index():
    '''The main page.
    '''
    words = '<h1>Zombie Raptor Launches on August 20th</h1><p>Expect awesome games from Zombie Raptor in the near future.</p>'

    page_title = heading

    css = 'night'

    return render_template('wiki.html',
                           style=css,
                           main_title=heading,
                           post=words,
                           title=page_title,
                           sidebar=navbar)

@app.route('/f')
def forums():
    page_title = '%s :: %s' % ('Forums', heading)

    sample = open(path.join(path.dirname(__file__), 'data', 'sample.yml'))
    thread = yaml.load(sample)
    sample.close()

    return render_template('forum.html', style='night', main_title=heading, posts=thread['posts'], sidebar=navbar, title=page_title, thread_title=thread['title'])

@app.route('/night.css')
def night():
    conf = open(path.join(path.dirname(__file__), 'data', 'style.yml'))
    style = yaml.load(conf)
    conf.close()

    response = make_response(render_template('main.css',
                                             text=style['text'],
                                             background=style['background'],
                                             post=style['post']))
    response.mimetype = 'text/css'
    return response
