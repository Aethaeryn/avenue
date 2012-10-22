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
navbar.append({'title'   : 'Zombie Raptor Blog',
               'content' : 'Read new updates from the Zombie Raptor team!',
               'link'    : '/'})

navbar.append({'title'   : 'Main Forum',
               'content' : 'Visit the main forum!',
               'link'    : '/f/main'})

browser_upgrade = '<p><img src="static/dl/firefox-g.png"></img><img src="static/dl/chrome-g.png"></img><img src="static/dl/safari-g.png"></img><img src="static/dl/opera-g.png"></img></p>'

tags = { 'post'  : ['post', '#aabbcc', '/'],
         'test'  : ['test', '#ffbb99', '/'],
         'micro' : ['micro', '#aabbcc', '/'],
         'link'  : ['link', '#aabbcc', '/'],
         'news'  : ['news', '#bbeebb', '/']}

def button(text):
    return '<div class="button">%s</div>' % text

buttons = '<p>%s%s%s%s&nbsp</p>' % (button(u'↳'), button('+'), button('-'), button('#'))

def render_forum(thread_title='', main_title='', html_title='', posts=[], threaded=False, content=''):
    return render_template('forum.html',
                           style='night',
                           sidebar=navbar,
                           thread_title=thread_title,
                           main_title=main_title,
                           html_title=html_title,
                           posts=posts,
                           threaded=threaded,
                           content=content)

@app.route('/')
def index():
    '''The main page.
    '''
    words = '<p>Expect stuff from Zombie Raptor in the near future.</p>'

    page_title = heading

    css = 'night'

    post = {'level' : 0, 'content' : words, 'author' : 'admin', 'date' : 'now'}

    return render_forum(main_title=heading,
                        thread_title="Zombie Raptor Launches... at some point.",
                        html_title=page_title,
                        posts=[post],
                        content='blog')

@app.route('/f/')
def f():
    return ''

@app.route('/f/main/')
def main_forum():
    main_forum_ = open(path.join(path.dirname(__file__), 'data', 'main_forum.yml'))
    test = yaml.load(main_forum_)
    main_forum_.close()

    page_title = '%s :: %s' % ('Main Forum', heading)

    for post in test['posts']:
        for i in range(len(post['tags'])):
            post['tags'][i] = tags[post['tags'][i]]

    return render_forum(main_title=heading + ' -- Main Forum',
                        thread_title='Active Threads',
                        html_title=page_title,
                        posts=test['posts'],
                        content='index')

@app.route('/f/main/post/')
def post():
    return ''

@app.route('/f/main/post/1')
def sample_post():
    sample = open(path.join(path.dirname(__file__), 'data', 'sample.yml'))
    thread = yaml.load(sample)
    sample.close()

    page_title = '%s :: %s :: %s' % (thread['title'], 'Main Forum', heading)

    return render_forum(main_title=heading + ' -- Main Forum',
                        thread_title=thread['title'],
                        html_title=page_title,
                        posts=thread['posts'],
                        threaded=True,
                        content='post')

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
