# FIFO = # First In - First Out (Primer en Entrar - Primero en Salir)
# Debo eliminar siempre el primero de la lista

# LIFO = # Last In - First Out (Ultimo en Entrar - Primero en Salir)
# Debo eliminar siempre el ultimo de la lista
from twilio.rest import Client

class Queue:

    def __init__(self):
        self.account_sid = 'ACfe217c9fa9007d8ff9e15ac384697987'
        self.auth_token = '45d52cd0d99d38bf2467efeccfcaf0f0'
        self.client = Client(self.account_sid, self.auth_token)
        self._queue = []
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = 'FIFO'

    def enqueue(self, item):
        self._queue.append(item)
        message = self.client.messages.create(
            body="Entraste en la fila! Hay " + str(len(self._queue)) + " persona(s) antes que tu",
            to="+56994341489",
            from_="+13392040838"
        )
        message.sid
        print(message.sid)
        print(self._queue)

    def dequeue(self):
        if self._mode == "FIFO":
            self._queue.pop(0)
            message = self.client.messages.create(
                body="Es tu turno!",
                to="+56994341489",
                from_="+13392040838"
            )
            message.sid
            print(message.sid)
            print(self._queue)
        else:
            self._queue.pop(len(_queue)-1)
            message = self.client.messages.create(
                body="Es tu turno!",
                to="+56994341489",
                from_="+13392040838"
            )
            message.sid
            print(message.sid)
            print(self._queue)
    def get_queue(self):
        pass #devuelve el _queue
    def size(self):
        return len(self._queue)


'''
message = client.messages.create(
         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
         to='+15558675310'
     )

print(message)


{
  "account_sid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "api_version": "2010-04-01",
  "body": "Join Earth's mightiest heroes. Like Kevin Bacon.",
  "date_created": "Thu, 30 Jul 2015 20:12:31 +0000",
  "date_sent": "Thu, 30 Jul 2015 20:12:33 +0000",
  "date_updated": "Thu, 30 Jul 2015 20:12:33 +0000",
  "direction": "outbound-api",
  "error_code": null,
  "error_message": null,
  "from": "+14155552345",
  "messaging_service_sid": "MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "num_media": "0",
  "num_segments": "1",
  "price": null,
  "price_unit": null,
  "sid": "MMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "status": "sent",
  "subresource_uris": {
    "media": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Media.json"
  },
  "to": "+15558675310",
  "uri": "/2010-04-01/Accounts/ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Messages/SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.json"
}

'''