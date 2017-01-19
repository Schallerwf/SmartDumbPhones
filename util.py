import re
import time

INVALID_COMMAND = 'Invalid command. Text "help" to see a list of valid commands.'
YES_OPTIONS = ['y', 'yes', 'yeah', 'yep', 'yes sir', 'yep', 'yah', 'ya', 'opposite of no',]

months = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'June': '06',
    'July': '07',
    'Aug': '08',
    'Sept': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12',
}


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

#example format - '18 Jan 2017 19:27:22'
def recievedTimeToEpoch(t):
    parts = t.split(' ')
    month = months[parts[1]]
    print month
    print parts
    hour = parts[3].split(':')
    print hour
    timeString = '{0}/{1} {3}/{2}/{4}'.format(hour[0], hour[1], parts[0], month, parts[2])
    print timeString
    pattern = '%H/%M %m/%d/%Y'
    return int(time.mktime(time.strptime(timeString, pattern)))
