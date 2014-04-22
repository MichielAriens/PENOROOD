import pika

class Sender:

    def __init__(self,broker='localhost'):
        connection = pika.BlockingConnection(pika.ConnectionParameters(broker))
        self.channel = connection.channel()

        self.channel.queue_declare(queue='roodQueue')

    def sendCommand(self,command='Hello World!'):
        self.channel.basic_publish(exchange='server',
                             routing_key='roodQueue',
                             body=command)
        print("Command sent.")    # remove this line after testing.

    def closeConnection(self):
        self.connection.close()