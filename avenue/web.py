# -*- coding: utf-8 -*-
# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Acts as an interface between what Flask serves and what goes on in
the rest of the application.
'''
from avenue import app, api
from avenue.database import content
from flask import render_template, make_response, redirect

def url_generator():
    '''This function acts on a list of URLs, a text rule for each URL,
    and a function that says what to do to that text rule to serve a
    page. The action_list associates a subset of URLs with a
    particular function to be used as the action for that group.
    '''
    data = api.read_data('forum')
    threads = data['threads']
    content.insert_data()

    themes = content.get_themes()
    nav = content.get_nav()
    tags = content.get_tags()
    redirects = content.get_urls()

    def forum_set_tags():
        '''Turns strings containing tag names into tag objects that
        can be used to generate HTML/CSS renderings of the tag.
        '''
        for thread in threads:
            for post in threads[thread]['posts']:
                if 'tags' in post:
                    for i in range(len(post['tags'])):
                        post['tags'][i] = tags[post['tags'][i]]

    def forum_page(name):
        '''Makes a forum page of the given thread name.
        '''
        thread = threads[name]

        html = '%s :: %s :: %s' % (thread['title'], data['forum'], data['site'])
        main = '%s -- %s' % (data['site'], data['forum'])

        title = { 'html'   : html,
                  'main'   : main,
                  'thread' : thread['title'],
                  'url'    : data['forum_url'] }

        return render_template('forum.html',
                               style='night',
                               sidebar=nav,
                               title=title,
                               posts=thread['posts'],
                               threaded=thread['threaded'])

    def setup_url_rule(urls, action):
        '''Sets up URL rules, given a dictionary of urls and a
        function that they will act on. It passes an anonymous
        function to add_url_rule that always does a particular action
        to a particular string when that URL is accessed.
        '''
        is_dict = type(urls) == dict

        for url in urls:
            text = urls[url] if is_dict else url
            app.add_url_rule(url, url, (lambda x: lambda: action(x))(text))

    forum_set_tags()

    css = {}

    for theme in themes:
        css[themes[theme]['url']] = theme

    setup_url_rule(redirects, redirect)
    setup_url_rule(css, lambda theme: api.make_css(themes[theme]))
    setup_url_rule(threads.keys(), forum_page)
