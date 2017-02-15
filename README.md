# SmartDumbPhones
Making dumb phones smart using python.

Works by taking advantage of the fact that my phone can text an email address.
I text an email 'SmartDumbPhones@gmail.com', a script on my computer polls for and processes messages and responds by emailing my phone through vtext.

## Examples
To get surf report for a beach: 'Surf in Morro Bay'
To get directions:              'Directions from 123 Fun Street to 567 Sandwich Street'
To check bitcoin price:         'bitcoin'
To set reminders:               'Textme Call Mom at 12/30'
To log a workout:               'I ran 5 miles'
To log a meal:                  'I ate a Cheese Burger'

## Limits
Vtext seems to have a bug where if an email text is in the process of being sent and you attempt to send another, the second request gets ignored and is never sent. So when texting from my phone, I need to space out my messages by ~30 seconds to be safe.
