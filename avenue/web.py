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

def forum_generator(site_name, forum_name):
    navbar = []
    navbar.append({'title'   : 'Zombie Raptor Blog',
                   'content' : 'Read new updates from the Zombie Raptor team!',
                   'link'    : '/'})

    navbar.append({'title'   : 'Main Forum',
                   'content' : 'Visit the main forum!',
                   'link'    : '/f/main'})

    tags = { 'post'  : ['post', '#aabbcc', '/'],
             'test'  : ['test', '#ffbb99', '/'],
             'micro' : ['micro', '#aabbcc', '/'],
             'link'  : ['link', '#aabbcc', '/'],
             'news'  : ['news', '#bbeebb', '/']}

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

    def forum_page(filename, content):
        data = open(path.join(path.dirname(__file__), 'data', filename))
        thread = yaml.load(data)
        data.close()

        html_title = '%s :: %s :: %s' % (thread['title'], forum_name, site_name)
        main_title = '%s -- %s' % (site_name, forum_name)

        for post in thread['posts']:
            if 'tags' in post:
                for i in range(len(post['tags'])):
                    post['tags'][i] = tags[post['tags'][i]]

        return render_forum(main_title=main_title,
                            thread_title=thread['title'],
                            html_title=html_title,
                            posts=thread['posts'],
                            threaded=thread['threaded'],
                            content=content)

    return forum_page

make_page = forum_generator('Zombie Raptor', 'Main Forum')

@app.route('/')
def index():
    return make_page('front_page.yml', 'blog')

@app.route('/f/')
def f():
    return ''

@app.route('/f/main/')
def main_forum():
    return make_page('main_forum.yml', 'index')

@app.route('/f/main/post/')
def post():
    return ''

@app.route('/f/main/post/1')
def sample_post():
    return make_page('sample.yml', 'post')


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
