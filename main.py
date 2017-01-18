from google import *
from handle import *
from util import *
from secret import *
from chron import *
import base64

def main():
    credentials = getCredentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    results = listMessagesWithLabels(service, 'me', ['UNREAD'])

    for result in results:
      curId = result.get('id')
      curEmail = service.users().messages().get(userId='me', id=curId).execute()
      fromEmail = curEmail.get('payload').get('headers')[3].get('value').replace('<', '').replace('>', '')
      if (fromEmail != myEmail):
        print 'Email from {0}. Ignorning.'.format(fromEmail)
        return
      toEmail = curEmail.get('payload').get('headers')[10].get('value')
      try:
        curRequest = base64.urlsafe_b64decode(curEmail.get('payload').get('body').get('data').encode("utf-8"))
        response = handle(curRequest, fromEmail)
        responseParts = splitMessage(response)
      except:
        responseParts = ['Error.']
      for part in responseParts:
        message = createMessage(toEmail, fromEmail, '', part)
        sendMessage(service, 'me', message)

      modifyMessage(service, 'me', curId, createMsgLabels())

    chronMessages = checkChronTasks()
    for message in chronMessages:
        responseParts = splitMessage(message)
        for part in responseParts:
            message = createMessage(thisEmail, myEmail, '', part)
            sendMessage(service, 'me', message)



if __name__ == '__main__':
    main()
