from util import *

eatDrinkWords = ['ate', '8', 'had', 'drank']
exerciseWords = ['biked', 'bike', 'rode', 'pedaled', 'ran', 'jogged', 'yoga', 'stretched', 'surfed', 'surf', 'swam', 'swimmed']

def personalTrackerByWord(message):
    try:
        parts = message.strip().split(' ')
        logPersonalLevel(parts[0], parts[1])
    except:
        return 'Error. Could not process that message.'
    return 'Logged successfully.'

def personalTracker(message):
    # We know first word in 'i'
    parts = message.split(' ')
    b = False

    try:
        restOfMessage = ' '.join(parts[2:])
        if parts[1] in eatDrinkWords:
            iAte(restOfMessage) 
            b = True
        if parts[1] in exerciseWords:
            iExercised(parts[1], restOfMessage)
            b = True
    except Exception as e:
        return 'Error. Could not process that message.'

    if b:
        return 'Logged successfully.'
    else: 
        return 'Not sure what you want me to log. Sorry.'

def iAte(item):
    if hasNumbers(item):
        parts = item.split(' ')
        logConsumable(int(parts[0]), ''.join(parts[1:]))
    else:
        logConsumable(1, item)

# expect something like, 'I swam for 5 hours'
def iExercised(activity, amount):
    amount = amount.replace('for', '').strip()
    parts = amount.split(' ')
    logExercise(activity, parts[0], parts[1])

def logExercise(activity, measurment, units):
    with open('ExerciseHistory', 'a') as output:
        output.write('{0},{1},{2},{3}\n'.format(now(),activity,measurment,units))

def logConsumable(number, item):
    with open('EatAndDrinkHistory', 'a') as output:
        output.write('{0},{1},{2}\n'.format(now(),item,number))

def logPersonalLevel(level, attribute):
    with open('PersonalHistory', 'a') as output:
        output.write('{0},{1},{2}\n'.format(now(),attribute,level))
