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

def read_data(filename):
    filename = '%s.yml' % filename

    data_file = open(path.join(path.dirname(__file__), 'data', filename))
    data = yaml.load(data_file)
    data_file.close()

    return data

def forum_generator(site, forum):
    navbar = read_data('navbar')
    tags = read_data('tags')
    threads = read_data('threads')

    def set_tags():
        for thread in threads:
            for post in threads[thread]['posts']:
                if 'tags' in post:
                    for i in range(len(post['tags'])):
                        post['tags'][i] = tags[post['tags'][i]]

    def render_forum(thread_title='', main_title='', html_title='',
                     posts=[], threaded=False, content=''):

        return render_template('forum.html',
                               style='night',
                               sidebar=navbar,
                               thread_title=thread_title,
                               main_title=main_title,
                               html_title=html_title,
                               posts=posts,
                               threaded=threaded,
                               content=content)

    def forum_page(name, content):
        thread = threads[name]

        html_title = '%s :: %s :: %s' % (thread['title'], forum, site)
        main_title = '%s -- %s' % (site, forum)

        return render_forum(main_title=main_title,
                            thread_title=thread['title'],
                            html_title=html_title,
                            posts=thread['posts'],
                            threaded=thread['threaded'],
                            content=content)

    set_tags()

    return forum_page

make_page = forum_generator('Zombie Raptor', 'Main Forum')

@app.route('/')
def index():
    return make_page('front_page', 'blog')

@app.route('/f/')
def f():
    return ''

@app.route('/f/main/')
def main_forum():
    return make_page('main_forum', 'index')

@app.route('/f/main/post/')
def post():
    return ''

@app.route('/f/main/post/1')
def sample_post():
    return make_page('sample', 'post')


@app.route('/night.css')
def night():
    style = read_data('style')

    response = make_response(render_template('main.css',
                                             text=style['text'],
                                             background=style['background'],
                                             post=style['post']))
    response.mimetype = 'text/css'
    return response
