import pika


"""
REALIZA A CONEXÃO COM O BROKER
"""
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

"""
REALIZA A CONEXÃO COM A FILA
"""
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(f"[x] Recebido {body}")

"""
REALIZA O CONSUMO DOS DADOS NA FILA "hello"
"""
channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

channel.start_consuming()