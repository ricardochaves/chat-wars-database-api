import pika

HOST = "amqps://ricardobchaves:password@api.chtwrs.com:5673"
QUEUE = "ricardobchaves_au_digest"


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


parameters = pika.URLParameters(HOST)


connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.basic_consume(queue=QUEUE, auto_ack=True, on_message_callback=callback)
