from confluent_kafka.admin import AdminClient, NewTopic, KafkaException
import time 

admin_client = AdminClient({
    'bootstrap.servers': 'localhost:9093',
    'client.id': 'topic-from-python'
})

# Función para crear tópicos
def crear_topico(nombre_topico):
    try:
        futures = admin_client.create_topics([NewTopic(nombre_topico, num_partitions=1, replication_factor=1)])
        for topic, future in futures.items():
            try:
                future.result()  # Espera a que se complete la creación del tópico
                print(f"Tópico '{topic}' creado exitosamente.")
            except KafkaException as e:
                print(f"Error al crear el tópico '{topic}': {e}")
    except Exception as e:
        print(f"Error al crear el tópico: {e}")

# Lista de tópicos a crear
topicos = ['compra_realizada', 'estado_actualizado']

# Crear cada tópico
for topico in topicos:
    crear_topico(topico)
    time.sleep(1)  # Espera un segundo entre creaciones para evitar sobrecarga

print("Todos los tópicos han sido creados.")