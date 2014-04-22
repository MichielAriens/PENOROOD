import pika

class zepListener:
	def __init__(self, zeppelin):
		self.zeppelin = zeppelin
		init()
		
	def callback(ch, method, properties, body):
		print(" [x] Received %r" % (body,))

	def init(self):
		creds = pika.PlainCredentials('rood','rood')
		connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=creds ))
		channel = connection.channel()
		channel.queue_declare(queue='hellorood')
		channel.basic_consume(callback,queue='hellorood',no_ack=True)
		channel.start_consuming()
			
	def pushPosition(self,pos):
		key = "rood.info.location"  
		myBody = pos[0]*10 + "," + pos[1]*10
		channel.basic_publish(exchange='server',
                      routing_key = key,
                      body = myBody)
		
	def pushHeight(self,pos):
		key = "rood.info.height"  
		myBody = pos * 10
		channel.basic_publish(exchange='server',
		              routing_key = key,
		              body = myBody)
		
			