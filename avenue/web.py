# -*- coding: utf-8 -*-
# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Acts as an interface between what Flask serves and what goes on in
the rest of the application.
'''
from avenue import app, api
from flask import render_template, make_response, redirect

def url_generator():
    '''This function acts on a list of URLs, a text rule for each URL,
    and a function that says what to do to that text rule to serve a
    page. The action_list associates a subset of URLs with a
    particular function to be used as the action for that group.
    '''
    forum_data = api.read_data('forum')

    def make_css(style):
        '''Reads style rules from a file and applies them to a css
        template to generate a css file.
        '''
        style = forum_data['style']

        response = make_response(render_template('main.css',
                                                 text=style['text'],
                                                 background=style['background'],
                                                 post=style['post']))
        response.mimetype = 'text/css'
        return response

    def forum_generator(site, forum):
        '''Reads in data files representing static forum states. Returns a
        function that accesses forum pages.
        '''
        navbar = forum_data['navbar']
        tags = forum_data['tags']
        threads = forum_data['threads']

        def set_tags():
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

            html_title = '%s :: %s :: %s' % (thread['title'], forum, site)
            main_title = '%s -- %s' % (site, forum)

            return render_template('forum.html',
                                   style='night',
                                   sidebar=navbar,
                                   main_title=main_title,
                                   thread_title=thread['title'],
                                   html_title=html_title,
                                   posts=thread['posts'],
                                   threaded=thread['threaded'],
                                   content=thread['content_type'])

        set_tags()

        return forum_page

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

    urls = forum_data['urls']

    make_page = forum_generator('Zombie Raptor', 'Main Forum')

    action_list = [('redirect', redirect),
                   ('forum_urls', make_page),
                   ('css', make_css)]

    for action in action_list:
        setup_url_rule(urls[action[0]], action[1])
