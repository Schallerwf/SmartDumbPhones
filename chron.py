import time
import os
from handle import *

def writeToChronTasks(taskName, data, timeToExecute):
    with open('chronTasks', 'a') as chronTasks:
        if taskName == 'textme':
            chronTasks.write('{0},{1},{2}'.format(timeToExecute, taskName, data))

def checkChronTasks():
    messagesToSend = []
    with open('chronTasks', 'r') as chronTasks, open('newChronTasks', 'w+') as newChronTasks:
        for line in chronTasks:
            parts = line.rstrip().split(',')
            if int(time.time()) >= int(parts[0]):
                messagesToSend.append(handleChron(parts[1], parts[2]))
            else:
                newChronTasks.write(line)
    os.rename('newChronTasks', 'chronTasks')
    return messagesToSend
