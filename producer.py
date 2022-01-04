import pika
import time

"""
REALIZA A CONEXÃO COM O BROKER
"""
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

"""
REALIZA A CONEXÃO COM A FILA
"""
channel.queue_declare(queue='hello')


messages = ['Primeira mensagem', 'Segunda mensagem','Terceira mensagem', 'Quarta mensagem','Quinta mensagem']

for message in messages:
    print( "Enviada [x] :",message)
    channel.basic_publish(exchange='', routing_key='hello', body=message)

"""
FINALIZA A CONEXÃO COM O BROKER
"""
connection.close()