import os, sys
from directions import *
from context import *
from util import *
from help import *
from bitcoin import *
from surfline import *
from personal import *
from secret import *

def handle(message, user):
    firstWord = message.split(' ')[0].lower()
    r = INVALID_COMMAND

    if (firstWord == 'directions'):
        r = startDirections(message)
    elif (firstWord == 'search'):
        r = search(message)
    elif (firstWord == 'translate'):
        r = translate(message)
    elif (firstWord == 'textme'):
        r = textMe(message)
    elif (firstWord == 'sendme'):
        r = sendMe(message)
    elif (firstWord == 'help'):
        r = helpMe(message)
    elif (firstWord == 'more'):
        r = handleViaContext(user)
    elif (firstWord == 'i'):
        r = personalTracker(message)
    elif (firstWord in personalTrackerWords):
        r = personalTrackerByWord(message)
    elif (message.strip().lower() in YES_OPTIONS):
        r = handleViaContext(user)
    elif (message.strip().lower() in SURF_STATUS):
        r = surfStatus(message)
    elif (message.strip().lower() == 'bitcoin price' or message.strip().lower() == 'bitcoin'):
        r = bitcoinPrice()
    elif (message.strip().lower() == 'entertain me'):
        r = entertain()

    writeContext(user, message)
    return r

def handleViaContext(user):
    context = getContext(user)
    firstWord = context.split(' ')[0].lower()
    r = INVALID_COMMAND

    if (firstWord == 'directions'):
        r = confirmDirections(context)
    elif (firstWord in SURF_STATUS):
        r = moreSurfInfo(context)

    return r

def handleChron(task, data):
    if task == 'textme':
        return data
