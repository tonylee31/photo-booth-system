import pika, sys, os


def main():
     credentials = pika.PlainCredentials('admin', '123456')
     parameters = pika.ConnectionParameters(host='localhost',
                                            port=5672,
                                            virtual_host='demo-vhost',
                                            credentials=credentials)
     connection = pika.BlockingConnection(parameters)
     channel = connection.channel()
     
     channel.queue_declare(queue='demo-queue',durable=True,passive=True)
     
     def callback(ch, method, properties, body):
     
         print(f" [x] Received {body.decode()}")
         # channel.basic_ack(method.delivery_tag)
     
     channel.basic_consume(queue='demo-queue',
                           auto_ack=True,
                           on_message_callback=callback)
     
     print(' [*] Waiting for messages. To exit press CTRL+C')
     
     try:
         channel.start_consuming()
     except KeyboardInterrupt:
         channel.stop_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        connection.close()
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
