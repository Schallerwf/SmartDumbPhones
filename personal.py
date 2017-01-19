from util import *

eatDrinkWords = ['ate', '8', 'had', 'drank']
exerciseWords = ['biked', 'bike', 'rode', 'pedaled', 'ran', 'jogged', 'yoga', 'stretched', 'surfed', 'surf', 'swam', 'swimmed']

def personalTrackerByWord(message, timeRecieved):
    try:
        parts = message.strip().split(' ')
        logPersonalLevel(parts[0], parts[1], timeRecieved)
    except:
        return 'Error. Could not process that message.'
    return 'Logged successfully.'

def personalTracker(message, timeRecieved):
    # We know first word in 'i'
    parts = message.split(' ')
    b = False

    try:
        restOfMessage = ' '.join(parts[2:])
        if parts[1] in eatDrinkWords:
            iAte(restOfMessage, timeRecieved) 
            b = True
        if parts[1] in exerciseWords:
            iExercised(parts[1], restOfMessage, timeRecieved)
            b = True
    except Exception as e:
        return 'Error. Could not process that message.'

    if b:
        return 'Logged successfully.'
    else: 
        return 'Not sure what you want me to log. Sorry.'

def iAte(item, time):
    if hasNumbers(item):
        parts = item.strip().rstrip().split(' ')
        logConsumable(int(parts[0]), ''.join(parts[1:]), time)
    else:
        logConsumable(1, item.strip().rstrip(), time)

# expect something like, 'I swam for 5 hours'
def iExercised(activity, amount, time):
    amount = amount.replace('for', '').strip()
    parts = amount.split(' ')
    logExercise(activity, parts[0], parts[1], time)

def logExercise(activity, measurment, units, time):
    with open('ExerciseHistory', 'ab') as output:
        output.write('{0},{1},{2},{3}\n'.format(time,activity,measurment,units))

def logConsumable(number, item, time):
    with open('EatAndDrinkHistory', 'ab') as output:
        output.write('{0},{1},{2}\n'.format(time,item,number))

def logPersonalLevel(attribute, level, time):
    with open('PersonalHistory', 'ab') as output:
        output.write('{0},{1},{2}\n'.format(time,attribute,level))
