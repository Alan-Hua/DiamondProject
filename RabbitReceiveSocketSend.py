import pika
import jsonpickle
import socket

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    dataEncoded = jsonpickle.encode(body)
    dataDecoded = jsonpickle.decode(dataEncoded)

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 8089))
    clientsocket.send(dataDecoded)

    print(" [x] Received %r" % dataEncoded)
    print("[x] Sent %r" % dataDecoded)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
