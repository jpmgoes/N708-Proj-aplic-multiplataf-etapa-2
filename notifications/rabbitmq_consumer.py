import pika

def consume_message():
    # Conexão com RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    # Declarando a fila (caso ela não exista)
    channel.queue_declare(queue='event_queue')

    # Função de callback que processa a mensagem
    def callback(ch, method, properties, body):
        print(f"Mensagem recebida: {body.decode()}")
        # Aqui você pode processar a mensagem conforme necessário

    # Consumir mensagens da fila
    channel.basic_consume(queue='event_queue', on_message_callback=callback, auto_ack=True)

    print('Aguardando mensagens...')
    channel.start_consuming()
