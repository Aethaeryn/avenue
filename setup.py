# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''This file does all of the actions necessary to set up Avenue before
running it for the first time.
'''
from os import path, listdir, mkdir
import requests

def location(*args):
    '''Turns a string that is a relative directory location into a
    full path that Python can understand.
    '''
    loc = path.dirname(__file__)

    for arg in args:
        loc = path.join(loc, arg)

    return loc

def static_setup():
    '''Adds needed directories if they don't already exist.
    '''
    if 'static' not in listdir(location('avenue')):
        mkdir(location('avenue', 'static'))

    if 'dl' not in listdir(location('avenue', 'static')):
        mkdir(location('avenue', 'static', 'dl'))

def get_icons():
    '''Gets browser icons if they don't already exist.
    '''
    icons = { 'firefox' : {'filename' : 'Mozilla_Firefox_3.5_logo_256.png',
                           'location' : 'commons'},

              'chrome'  : {'filename' : 'Google_Chrome_2011_computer_icon.svg',
                           'location' : 'en'},

              'safari'  : {'filename' : 'Apple_Safari.png',
                           'location' : 'en'},

              'opera'   : {'filename' : 'Opera_O.svg',
                           'location' : 'commons'}}

    for browser in icons:
        stats = ('upload.wikimedia.org/wikipedia/',
                 icons[browser]['location'],
                 icons[browser]['filename'],
                 icons[browser]['filename'])

        url = 'http://%s%s/thumb/f/fa/%s/128px-%s' % stats

        loc = location('avenue', 'static', 'dl', browser + '.png')

        if browser + '.png' not in listdir((location('avenue', 'static', 'dl'))):
            destination = open(loc, 'w')
            destination.write(requests.get(url).content)
            destination.close()

def main():
    '''Sets up various things that are required for running Avenue.
    '''
    static_setup()
    get_icons()

if __name__ == '__main__':
    main()
