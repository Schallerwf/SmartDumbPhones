import re

INVALID_COMMAND = 'Invalid command. Text "help" to see a list of valid commands.'

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
