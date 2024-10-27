import grpc
from concurrent import futures
import time
import kafka
import pedido_pb2
import pedido_pb2_grpc

class GestionPedidos(pedido_pb2_grpc.GestionPedidosServicer):

    def __init__(self, kafka_topic):
        self.producer = kafka.KafkaProducer(bootstrap_servers='localhost:9092')
        self.kafka_topic = kafka_topic

    def RealizarCompra(self, request, context):
        # Publicar en Kafka
        mensaje = {
            'cliente': request.cliente,
            'producto': request.producto,
            'precio': request.precio,
            'pasarela_pago': request.pasarela_pago,
            'marca_tarjeta': request.marca_tarjeta,
            'banco': request.banco,
            'comuna': request.comuna,
            'direccion': request.direccion,
            'email': request.email,
        }
        
        self.producer.send(self.kafka_topic, value=mensaje)
        self.producer.flush()

        return pedido_pb2.Respuesta(mensaje="Compra realizada con éxito", exito=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pedido_pb2_grpc.add_GestionPedidosServicer_to_server(GestionPedidos('mi_tema_kafka'), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(86400)  # Mantener el servidor activo
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
