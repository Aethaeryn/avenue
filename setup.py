# Copyright (c) 2012 Michael Babich
# See LICENSE.txt or http://opensource.org/licenses/MIT

'''This file does all of the actions necessary to set up Avenue before
running it for the first time.
'''
from os import path, listdir, mkdir

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

def main():
    '''Sets up various things that are required for running Avenue.
    '''
    static_setup()

if __name__ == '__main__':
    main()
