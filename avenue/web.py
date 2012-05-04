# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Acts as an interface between what Flask serves and what goes on in
the rest of the application.
'''
from avenue import app, api
from flask import render_template
from copy import copy

heading = 'Zombie Raptor'
navbar = []
navbar.append({'title'   : 'Federation',
               'content' : 'Form federations with your friends and plot to take over the galaxy!',
               'link'    : '/'})
navbar.append({'title'   : 'Zombie Raptor Blog',
               'content' : 'Read new updates from the Zombie Raptor team!',
               'link'    : '/'})
navbar.append({'title'   : 'Forums',
               'content' : 'Visit the official forums!',
               'link'    : '/'})

@app.route('/')
def index():
    navtile = copy(navbar)
    navtile.insert(0, {'title'    : 'Avenue',
                       'content'  : 'Read about Avenue.',
                       'link'     : '/about'})

    page_title = heading

    print 'ugh'

    return render_template('tiles.html', 
                           style='static/dark-plain',
                           main_title=heading,
                           title=page_title,
                           tiles=navtile)


@app.route('/about')
def about():
    '''Serves a page describing Avenue.
    '''
    page_title = '%s :: %s' % ('Welcome to Avenue', heading)

    words = '<h1>Welcome to Avenue</h1><p>Avenue is a new way to run a ' \
    'website. Don\'t run many independent web applications that are designed '\
    ' for their own, isolated ecosystems! Avenue makes your life simple by '\
    'providing minimalist content systems that integrate seamlessly into one '\
    'Python web application with one database. No content mode is more '\
    'privileged than another. With Avenue, you\'re not forced to use an '\
    'application for something that it\'s not designed for. You don\'t get a '\
    'good user experience if you try to discuss in a wiki application or '\
    'blog in a forum application.</p><p>Everything fits together in one '\
    'website with a shared theme set and a unified account system. The '\
    'entire site just works out of the box without having to hand-modify or '\
    'install any plugins to get different apps, intended for different '\
    'purposes, to talk to each other. There\'s a consistent user interface, '\
    'too. Of course, if you want to extend Avenue, it is designed to handle '\
    'that. It should be able to support browser-based HTML 5 games, web '\
    'email, and possibly even IRC clients!</p><p>Avenue is convergence for '\
    'web apps. Why handle text a dozen different ways if you don\'t have '\
    'to?</p>'

    return render_template('article.html',
                           style='static/dark-plain',
                           main_title=heading,
                           post=words,
                           sidebar=navbar,
                           title=page_title)
