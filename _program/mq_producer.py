import pika
from datetime import datetime


credentials = pika.PlainCredentials('admin', '123456')
parameters = pika.ConnectionParameters(host='localhost',
                                       port=5672,
                                       virtual_host='demo-vhost',
                                       credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='demo-queue',durable=True,passive=True)


# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%Y%m%d%H%M%S")


for i in range(10):
    msg = dt_string + '-' + str(i)
    channel.basic_publish(exchange='', 
                          routing_key='demo-queue', 
                          body=msg)
    print(f" [x] Sent '{msg}'")

connection.close()