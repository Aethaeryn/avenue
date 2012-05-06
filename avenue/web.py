# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''Acts as an interface between what Flask serves and what goes on in
the rest of the application.
'''
from avenue import app, api
from flask import render_template, make_response
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
               'link'    : '/f'})

@app.route('/')
def index():
    navtile = copy(navbar)
    navtile.insert(0, {'title'    : 'Avenue',
                       'content'  : 'Read about Avenue.',
                       'link'     : '/about'})

    page_title = heading

    return render_template('tiles.html', 
                           style='night',
                           main_title=heading,
                           title=page_title,
                           tiles=navtile)

@app.route('/about')
def about():
    '''Serves a page describing Avenue.
    '''
    page_title = '%s :: %s' % ('Welcome to Avenue', heading)

    words = '<h1>Welcome to Avenue</h1><p><a href="/">Avenue</a> is a new way to run a ' \
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
    'to?</p><p>This text needs to be significantly expanded in order to fully test out all of the styling features that are present because I need to be able to test out everything and this requires long paragraphs and stuff.</p>'

    return render_template('wiki.html',
                           style='night',
                           main_title=heading,
                           post=words,
                           sidebar=navbar,
                           title=page_title)

@app.route('/f')
def forums():
    page_title = '%s :: %s' % ('Forums', heading)

    post_list = ['When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature\'s God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation.', 'We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness. -- That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, -- That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness. Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes; and accordingly all experience hath shewn, that mankind are more disposed to suffer, while evils are sufferable, than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same Object evinces a design to reduce them under absolute Despotism, it is their right, it is their duty, to throw off such Government, and to provide new Guards for their future security.']

    return render_template('forum.html', style='night', main_title=heading, posts=post_list, sidebar=navbar, title=page_title)

@app.route('/night.css')
def night():
    text1 = {'plain' : '#111111',
             'link'  : '#0438a0',
             'hover' : '#0853e1',
             'heading' : '#ff7f24',
             'head_hover' : '#df4f14',
             'nav' : '#d6d9d9',
             'nav_hover' : '#aaaaaa'}

    background1 = {'plain' : '#000000',
                   'post'  : '#d6d9d9',
                   'box1'  : '#1a1123'}

    response = make_response(render_template('main.css', text=text1, background=background1))
    response.mimetype = 'text/css'
    return response
