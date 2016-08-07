from util import INVALID_COMMAND

HELP_MESSAGE = 'Valid commands are [directions, search, translate, textme, ' \
  'help, bitcoin price, entertain me]. Text help <command> to see information specific to each command.'

def helpMe(message):
    if (message.strip() == 'help'):
        return HELP_MESSAGE

    command = message.replace('help', '').strip()

    r = INVALID_COMMAND
    if (command == 'directions'):
        r = 'Format: directions from <origin> to <destination>\n'
        r +=  'Purpose: Sends step by step directions between two locations via text.'
    elif (command == 'search'):
        r = 'Format: search <search-terms>\n'
        r += 'Purpose: Performs a google search and returns a summary response.'
    elif (command == 'translate'):
        r = 'Format: translate: <text-to-be-translated> to <target-language>\n'
        r += 'Purpose: Translates text to a target language.'
    elif (command == 'textme'):
        r = 'Format: textme <message> at <time> from <from>\n'
        r += 'Purpose: Send yourself a message at a certain time. "At" and "from" are optional ' \
        'and default to now and SmartDumbPhones@gmail.com respectivly.'
    elif (command == 'help'):
        r = 'Format: help <optional-command>\n'
        r += 'Purpose: Print helpful information like the text you are reading right now!'
    elif (message.strip().tolower() == 'bitcoin price'):
        r = 'Format: bitcoin price\n'
        r += 'Purpose: Get the current price of bitcoin in USD.'
    elif (message.strip().tolower() == 'entertain me'):
        r = 'Format: entertain me\n'
        r += 'Purpose: Bored with your dumb phone? Get a little entertainment.'

    return r