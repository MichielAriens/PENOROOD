import pika

class zepListener:
    def __init__(self, zeppelin):
        self.zeppelin = zeppelin

    #def callback(ch, method, properties, body):
    #    print(" [x] Received %r" % (body,))

    def start(self):
        self.creds = pika.PlainCredentials('rood', 'rood')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=self.creds))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='topic_logs',
                         type='topic')
        self.result = self.channel.queue_declare(exclusive=True)
        self.queue_name = self.result.method.queue
        self.channel.queue_bind(exchange='server',
                   queue=self.queue_name,
                   routing_key="#")
        self.channel.basic_consume(self.callback,
                      queue=self.queue_name,
                      no_ack=True)
        self.channel.start_consuming()
        print "listener listening"

    def callback(self, ch, method, properties, body ):
        #print " [x] %r:%r" % (method.routing_key, body,)
        pass

    def pushPosition(self, pos):
        print "pushing pos: " + str(pos)
        key = "rood.info.location"
        myBody = str(pos[0] * 10) + "," + str(pos[1] * 10)
        self.channel.basic_publish(exchange='server', routing_key=key, body=myBody)

    def pushHeight(self, pos):
        pos = int(float(pos))
        print "pushing height: " + str(pos)
        key = "rood.info.height"
        myBody = str(pos * 10)
        self.channel.basic_publish(exchange='server', routing_key=key, body=myBody)
		
			