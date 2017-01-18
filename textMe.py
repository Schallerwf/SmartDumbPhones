import time
from chron import *

def textMe(message):
    messageToText = findBetween(message, 'textme', 'at')
    time = findBetween(message, 'at', '')

    targetEpoch = parseTime(time)

    writeToChronTasks('textMe', messageToText, targetEpoch)
     
    return r

def parseTime(time):
    smallPattern = '%H/%M'
    largePattern = '%H/%M %m/%d%/y' 
    if len(time) > 6:
        return int(time.mktime(time.strptime(time, largePattern)))
    else:
        return int(time.mktime(time.strptime(time, smallPattern)))
