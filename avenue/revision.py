'''Uses difflib to create a revision system of text files so that only
the most recent revision is saved in complete form, using a diff for
the older revisions.
'''
from difflib import unified_diff

def diff(string1, string2):
    '''Returns a compact diff string of the two strings provided.
    '''
    def _string_to_list(string):
        '''Converts the string into a list with a trailing newline,
        which is the form that unified_diff() understands.
        '''
        if string[-1] != '\n':
            string = '%s%s' % (string, '\n')

        return string.splitlines(True)

    return ''.join(list(unified_diff(_string_to_list(string1),
                                     _string_to_list(string2))))
