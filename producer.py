from confluent_kafka import Producer
import time
import json
from uuid import uuid4
from generar_compra import generar_compra  # Importa la función desde generar_compra.py

# Configura el Producer para conectarse a los brokers
producer_conf = {
    'bootstrap.servers': 'localhost:9093',  # Cambia al puerto correcto si es necesario
    'client.id': 'productor1'
}
producer = Producer(producer_conf)

def delivery_report(err, msg):
    if err is not None:
        print(f"Error al entregar mensaje: {err}")
    else:
        print(f"Mensaje enviado a {msg.topic()} [{msg.partition()}]")

for _ in range(100):
    compra_aleatoria = generar_compra()  # Usa la función de generar_compra
    message = json.dumps(compra_aleatoria)  # Convierte la compra a JSON
    key = str(uuid4())
    
    print(f"Key: {key} Produciendo mensaje: {message}")
    
    # Publica el mensaje en el tópico de Kafka
    producer.produce('compra_realizada', key=key, value=message, callback=delivery_report)
    
    # Poll para la entrega de mensajes
    producer.poll(0)
    time.sleep(1)

# Espera a que todos los mensajes pendientes sean entregados
producer.flush()

