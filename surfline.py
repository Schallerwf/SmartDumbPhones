import requests
from util import *

SURF_STATUS = ['surfline', 'surfstatus', 'surf status' 'surf']

spotMap = {'morro bay': 4193, 
           'morro': 4193,
           'pismo': 5065,
           'list': 0}

def surfStatus(message):
    return processMessage(message, False)

def moreSurfInfo(message):
    return processMessage(message, True)

def processMessage(message, verbose):
    locKey = getLocationKey(message)
    if (locKey == -1):
        return 'Error: Invalid Beach. To see a list of valid beaches, reply "surfstatus list".'
    if (locKey == 0):
        validBeaches = list(spotMap.keys())
        validBeaches.remove('list')
        return 'Valid Beaches: ' + str(validBeaches)

    response = requests.get('http://api.surfline.com/v1/forecasts/'+str(locKey)+'?resources=surf,analysis&days=1&getAllSpots=false&units=e&interpolate=false&showOptimal=false',verify=True)
    info = response.json()
    
    if (verbose):
        return stripHtmlTags(info['Analysis']['short_term_forecast'])
    else:
        s = info['Analysis']['generalCondition'][0] + '\n'
        return s + info['Analysis']['surfRange'][0]

def getLocationKey(message):
    message = message.strip().lower()
    for key in SURF_STATUS:
        message = message.replace(key, '')

    return spotMap.get(message.strip(), -1)