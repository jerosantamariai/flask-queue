# FIFO = # First In - First Out (Primer en Entrar - Primero en Salir)
# Debo eliminar siempre el primero de la lista

# LIFO = # Last In - First Out (Ultimo en Entrar - Primero en Salir)
# Debo eliminar siempre el ultimo de la lista
from twilio.rest import Client

class Queue:

    def __init__(self):
        self.account_sid = 'tienes que obtener tu info'
        self.auth_token = 'tienes que obtener tu info'
        self.client = Client(self.account_sid, self.auth_token)
        self._queue = [
            {
                "name": "Jeronimo1",
                "phone": "+56999999999"
            },
            {
                "name": "Jeronimo2",
                "phone": "+56999999999"
            },
            {
                "name": "Jeronimo3",
                "phone": "+56999999999"
            }
        ]
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = 'FIFO'

    def enqueue(self, item):
        self._queue.append(item)
        
        message = self.client.messages.create(
            body = "Hola " + item["name"] + "!, entraste en la fila! Eres el numero " + str(len(self._queue)) + " de la fila! Espera tu turno que ya te llamaremos!",
            to = item["phone"],
            from_ = "+56999999999"  #Tu numero de twilio
        )
        message.sid
        print(message.sid)
        print(self._queue)

    def dequeue(self):
        if self._mode == "FIFO":
            item = self._queue.pop(0)
            message = self.client.messages.create(
                body = "Hola " + item["name"] + " Es tu turno!",
                to = item["phone"],
                from_ = "+56999999999"
            )
            message.sid
            print(message.sid)
            print(self._queue)
        else:
            item = self._queue.pop()
            message = self.client.messages.create(
                body = "Hola " + item["name"] + " Es tu turno!",
                to = item["phone"],
                from_ = "+56999999999"
            )
            message.sid
            print(message.sid)
            print(self._queue)
    
    def get_queue(self):
        return self._queue
    
    def size(self):
        return len(self._queue)