from confluent_kafka import Consumer, Producer  # Importar también el Producer
from estados import EstadoPedido  # Importar la clase de estados
import json

# Configuración del productor
producer_conf = {
    'bootstrap.servers': 'localhost:9092',  # Cambia al puerto correcto si es necesario
    'client.id': 'consumidor1'
}
producer = Producer(producer_conf)  # Crear una instancia del Producer

# Configuración del consumidor
consumer_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mi_grupo',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_conf)
consumer.subscribe(['compra_realizada'])

def enviar_estado_actualizado(pedido_id, estado):
    # Función para publicar el estado actualizado en el tópico estado_actualizado
    producer.produce('estado_actualizado', value=json.dumps({'pedido_id': pedido_id, 'estado': estado}))
    producer.flush()

def procesar_compra(mensaje):
    # Procesar el mensaje de compra y gestionar el cambio de estado
    pedido = json.loads(mensaje.value())
    pedido_id = pedido['id']  # Asumiendo que cada pedido tiene un ID único
    estado_pedido = EstadoPedido()  # Crear una nueva instancia para el pedido

    # Simulación del procesamiento de la compra
    estado_pedido.mostrar_estado()  # Estado inicial

    # Avanzar al siguiente estado
    estado_pedido.siguiente_estado()
    estado_pedido.mostrar_estado()  # Mostrar el nuevo estado

    # Enviar el estado actualizado al tópico
    enviar_estado_actualizado(pedido_id, estado_pedido.estado_actual())

# Escucha los mensajes del tópico compra_realizada
while True:
    mensaje = consumer.poll(1.0)  # Espera un mensaje
    if mensaje is None:
        continue
    if mensaje.error():
        print(f"Error: {mensaje.error()}")
        continue

    procesar_compra(mensaje)

