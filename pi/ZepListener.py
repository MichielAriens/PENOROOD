import pika
import thread


class zepListener:
    def __init__(self, zeppelin):
        self.zeppelin = zeppelin

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % (body,))

    def start(self):
        self.creds = pika.PlainCredentials('rood', 'rood')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=self.creds))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='server',
                                  type='topic')
    #self.channel.basic_consume(self.callback,queue='hellorood',no_ack=True)
    #self.channel.start_consuming()
    #print "listener listening"

    def pushPosition(self, pos):
        print "pushing pos: " + str(pos)
        key = "rood.info.location"
        myBody = str(pos[0] * 10) + "," + str(pos[1] * 10)
        self.channel.basic_publish(exchange='server', routing_key=key, body=myBody)

    def pushHeight(self, pos):
        print "pushing height: " + str(pos)
        key = "rood.info.height"
        myBody = str(pos * 10)
        self.channel.basic_publish(exchange='server', routing_key=key, body=myBody)
		
			