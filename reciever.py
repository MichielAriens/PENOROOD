#import pika

creds = pika.PlainCredentials('rood','rood')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=creds ))
channel = connection.channel()

channel.queue_declare(queue='hellorood')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % (body,))

channel.basic_consume(callback,queue='hellorood',no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()