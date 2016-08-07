import re

INVALID_COMMAND = 'Invalid command. Text "help" to see a list of valid commands.'
YES_OPTIONS = ['y', 'yes', 'yeah', 'yep', 'yes sir', 'yep', 'yah', 'ya', 'opposite of no',]

def findBetween(string, first, last):
    try:
        start = string.index( first ) + len( first )
        if (last == ''):
            end = len(string)
        else:
            end = string.index( last, start ) 
        return string[start:end]
    except ValueError:
        return ''

def stripHtmlTags(text):
    return re.sub('<[^<]+?>', '', text)

def splitMessage(message):
    parts = []
    while message:
        parts.append(message[:120])
        message = message[120:]
    return parts
