import pika

def publish_message(message):
    # Conexão com RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    # Declarando a fila (caso ela não exista)
    channel.queue_declare(queue='event_queue')

    # Enviar mensagem
    channel.basic_publish(exchange='',
                          routing_key='event_queue',
                          body=message)
    print(f"Mensagem enviada: {message}")

    # Fechar conexão
    connection.close()
