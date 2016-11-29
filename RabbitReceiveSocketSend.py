import pika
import json
import jsonpickle
import socket

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    data = jsonpickle.encode(body)
    print(" [x] Received %r" % data)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

s = socket.socket()
host = socket.gethostname()
