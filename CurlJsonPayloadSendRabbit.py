import pika
import urllib.request
import json

request = urllib.request.Request("http://httpbin.org/get")
response = urllib.request.urlopen(request)
encoding = response.info().get_content_charset('utf8')
data = json.loads(response.read().decode(encoding))
data = json.dumps(data)


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=data)
print(" [x] Sent 'data'")
connection.close()
