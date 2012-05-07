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
    'to?</p>'

    return render_template('wiki.html',
                           style='night',
                           main_title=heading,
                           post=words,
                           sidebar=navbar,
                           title=page_title)

@app.route('/micro')
def micro():
    page_title = '%s :: %s' % ('Micro', 'Zombe Raptr')

    words = '<h2>This is a message that\'s exactly 140 characters long, which is a good size for a micro post for some strange reason that I don\'t understand!</h2>'

    return render_template('wiki.html',
                           style='night',
                           main_title=heading,
                           post=words,
                           sidebar=navbar,
                           title=page_title)

@app.route('/f')
def forums():
    page_title = '%s :: %s' % ('Forums', heading)

    thread_title = 'This is a Sample Thread'

    post_list = ['<p>The forums will go here eventually. I\'m just testing things out now.</p>',
                 '<p>Well, I could\'ve just put a note explaining that this website is just full of static filler stuff as I finalize the design aspect of Avenue, but then I realized that this site\'s purpose is to render text. So, I can simply write that explanation here in a verbose way. That way, I can test out posts of all different sizes to see how the theme renders.</p>', '<p>Fortunately, this is easier than it looks.</p>',
                 '<p>So a typical forum thread would look like this, except hopefully people would put lengthier posts here. The site and the software this site is built on top of are still being written, so this is just placeholder text. That means that this site doesn\'t actually work yet. Please don\'t be angry if one of the links doesn\'t work because nothing really works here yet. It\'s just sample text.</p>',
                 '<p>The thing is, I need to have a lot of text and a lot of posts in order to fully test out how everything is going to work or else I will not be able to account for all situations. I could put nonsense here or just some section from a public domain work, but to be honest, writing nonsense text is actually pretty easy.</p><p>Besides, this way I can try to think of all of the typical use cases that a forum might see in terms of posts and try to write as many different types of posts here. This will provide variety in testing.</p>', '<p>So, hopefully any style bugs will show up now before this is used by other people in a production environment.</p>',
                 '<p>Almost there! I just need to fill up an entire page!</p>',
                 '<p>Now, I am going to cheat a bit and have a bunch of one-liners.</p>',
                 '<p>Alright!</p>',
                 '<p>So this is what a page looks like when you have more posts than can fit on a typical screen. This is just the "flat" view. The threaded view is a little more complicated and so I will have to code it later.</p>']

    posts = []

    for post in post_list:
        posts.append({'content' : post, 'level' : 0})

    posts[1]['level'] = 1
    posts[2]['level'] = 2
    posts[4]['level'] = 1
    posts[5]['level'] = 2
    posts[7]['level'] = 1
    posts[8]['level'] = 2

    post_author = 'Michael | -1 year ago | reply'

    return render_template('forum.html', style='night', main_title=heading, posts=posts, sidebar=navbar, title=page_title, author=post_author, thread_title=thread_title)

@app.route('/night.css')
def night():
    text1 = {'plain' : '#111111',
             'link'  : '#0438a0',
             'hover' : '#0853e1',
             'heading' : '#ff7f24',
             'head_hover' : '#df4f14',
             'nav' : '#d6d9d9',
             'nav_hover' : '#aaaaaa'}

    background1 = {'plain'   : '#000000',
                   'post'    : '#c6c9c9',
                   'article' : '#d6d9d9',
                   'box1'    : '#1a1123'}

    response = make_response(render_template('main.css', text=text1, background=background1))
    response.mimetype = 'text/css'
    return response
