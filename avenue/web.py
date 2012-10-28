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

    print nav

    def forum_set_tags():
        '''Turns strings containing tag names into tag objects that
        can be used to generate HTML/CSS renderings of the tag.
        '''
        for thread in threads:
            for post in threads[thread]['posts']:
                if 'tags' in post:
                    for i in range(len(post['tags'])):
                        post['tags'][i] = data['tags'][post['tags'][i]]

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
        '''Sets up URL rules, given a dictionary of urls and a function
        that they will act on.
        '''
        def url_page_function(text):
            '''Returns a function that is associated with the URL
            page. This function is called when the URL page is
            requested. The anonymous (lambda) function does a
            particular action given a particular string, text. It's
            set up this way because the text fed into the action
            function is always the same for a particular web page.
            '''
            return lambda: action(text)

        for url in urls:
            app.add_url_rule(url, url, url_page_function(urls[url]))

    forum_set_tags()

    action_list = [('redirect', redirect),
                   ('forum_urls', forum_page),
                   ('css', lambda theme:
                        api.make_css(themes[theme]))]

    for action in action_list:
        setup_url_rule(data['urls'][action[0]], action[1])
