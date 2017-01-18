import re
import time

INVALID_COMMAND = 'Invalid command. Text "help" to see a list of valid commands.'
YES_OPTIONS = ['y', 'yes', 'yeah', 'yep', 'yes sir', 'yep', 'yah', 'ya', 'opposite of no',]

def findBetween(string, first, last):
    try:
        start = string.index( first ) + len( first )
        if (last == ''):
            end = len(string)
        else:
            end = string.rfind(last) 
        return string[start:end]
    except ValueError:
        return ''

def stripHtmlTags(text):
    return re.sub('<[^<]+?>', '', text.replace('&#160;', ''))

def splitMessage(message):
    parts = []
    ndx = 0 
    if len(message) < 121:
        return [message]
    while message:
        parts.append('({0})'.format(ndx) + message[:115])
        message = message[115:]
        ndx += 1
    return parts

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def now():
    return int(time.time())
