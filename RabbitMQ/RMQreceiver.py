import pika

class Receiver:

    def __init__(self,broker='localhost'):
        creds = pika.PlainCredentials('rood','rood')
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=broker,credentials=creds ))
        channel = connection.channel()

        channel.queue_declare(queue='roodQueue')
        channel.basic_consume(self.callback,queue='roodQueue',no_ack=True)

    def callback(ch, method, properties, body):
        print " [x] Received %r" % (body,)

    def startReceiving(self):
        print ' [*] Waiting for messages. To exit press CTRL+C'
        self.channel.start_consuming()

