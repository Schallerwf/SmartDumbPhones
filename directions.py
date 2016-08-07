import googlemaps
from datetime import datetime
from secret import secret
from util import findBetween, stripHtmlTags

def startDirections(message):
	directionsResult = directions(message)
	if (directionsResult == ''):
		return "Error. Please be more specific. <street-or-establishment>, <city-or-zip>, <state>."

	response = 'From: ' + directionsResult[0].get('legs')[0].get('start_address')
	response += '\nTo: ' + directionsResult[0].get('legs')[0].get('end_address')
	response += '\nDistance: ' + directionsResult[0].get('legs')[0].get('distance').get('text')
	response += '\nDuration: ' + directionsResult[0].get('legs')[0].get('duration').get('text') 
	response += '\nDoes this seem correct? (yes/no)'

	return response

def confirmDirections(message):
	directionsResult = directions(message)
	response = ''
	for step in directionsResult[0].get('legs')[0].get('steps'):
		response += stripHtmlTags(step.get('html_instructions')) + '\n'
	return response

def directions(message):
	gmaps = googlemaps.Client(key=secret())

	origin = findBetween(message, 'from', 'to')
	destination = findBetween(message, 'to', '')

	if (origin == '' or destination == ''):
		return 'Invalid message. Follow: directions from <origin> to <destination>.'

	now = datetime.now()
	return gmaps.directions(origin,
                                     destination,
                                     mode='driving',
                                     departure_time=now)
	