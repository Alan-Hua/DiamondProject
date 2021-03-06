import pika
import jsonpickle
import socket
import ssl

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    dataEncoded = jsonpickle.encode(body)#encodes the body so the received data is in a json string
    dataDecoded = jsonpickle.decode(dataEncoded)#decodes the dataEncoded so that it can be sent through the socket
#creates the socket part of this file
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 8089))
    clientsocket.send(dataDecoded)
    print(" [x] Received %r" % dataEncoded)
    print(" [x] Sent %r" % dataDecoded)
    # wrappedSocket = ssl.wrap_socket(clientsocket, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")#wraps socket with ssl protocol
    # wrappedSocket.connect(('localhost', 8089))
    # wrappedSocket.send(dataDecoded) #sends decoded data through

channel.basic_consume(callback, queue='hello', no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
