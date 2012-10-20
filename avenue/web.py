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

def button(text):
    return '<div class="button">%s</div>' % text

buttons = '<p>%s%s%s%s&nbsp</p>' % (button(u'↳'), button('+'), button('-'), button('#'))

@app.route('/')
def index():
    '''The main page.
    '''
    words = '<p>Expect stuff from Zombie Raptor in the near future.</p>'

    page_title = heading

    css = 'night'

    post = {'level' : 0, 'content' : words, 'author' : 'admin', 'date' : 'now'}

    return render_template('forum.html',
                           style=css,
                           main_title=heading,
                           posts=[post],
                           title=page_title,
                           thread_title="Zombie Raptor Launches... at some point.",
                           sidebar=navbar,
                           content='blog')

@app.route('/f/')
def f():
    return ''

@app.route('/f/main/')
def main_forum():
    test = [{'level' : 0, 'content' : '<h1 class="post-link"><a href="/f/main/post/1">This is a Sample Thread</a></h1><div class="tags">&nbsp;<span class="tag-content" style="background-color: #aabbcc">&nbsp;post&nbsp;</span> <span class="tag-content" style="background-color:#ffbb99">&nbsp;test&nbsp;</span></div>', 'author' : 'John', 'date' : '1 day ago'},
            {'level' : 0, 'content' : '<h1><a href="http://example.com/">test post please ignore</a></h1>', 'author' : 'obviously_original_content', 'date' : '3 years ago'},
            {'level' : 0, 'content' : '<h1><a href="http://example.com/">Hey guys, I think I might have discovered a new continent!</a></h1>', 'author' : 'christopher', 'date' : '520 years ago'}]

    return render_template('forum.html',
                           style='night',
                           main_title=heading + ' -- Main Forum',
                           thread_title='Active Threads',
                           posts=test,
                           sidebar=navbar,
                           content='index')

@app.route('/f/main/post/')
def post():
    return ''

@app.route('/f/main/post/1')
def sample_post():
    page_title = '%s :: %s' % ('Forums', heading)

    sample = open(path.join(path.dirname(__file__), 'data', 'sample.yml'))
    thread = yaml.load(sample)
    sample.close()

    return render_template('forum.html',
                           style='night',
                           main_title=heading + ' -- Main Forum',
                           posts=thread['posts'],
                           sidebar=navbar,
                           title=page_title,
                           thread_title=thread['title'],
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
