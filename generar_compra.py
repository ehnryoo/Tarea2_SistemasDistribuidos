import random
import sqlite3
import grpc
import pedido_pb2
import pedido_pb2_grpc

# Definición de datos fijos
pasarela_pago = ['MercadoPago', 'Webpay', 'Flow', 'Transbank', 'OnePay', 'Servipag', 'Pagofacil']

marca_tarjeta = ['VISA', 'Mastercard', 'AMEX', 'Magna', 'Diners Club']

banco = [
    'Banco de Chile', 'Banco Estado', 'Banco Santander', 'Banco BCI', 
    'Scotiabank', 'Itaú', 'Banco Ripley', 'Banco Falabella', 
    'Banco Consorcio', 'Banco Security', 'Banco Internacional', 'Banco BICE'
]

# Conexión a la base de datos Clientes.db
conn_clientes = sqlite3.connect('Datasets/Clientes.db')
cursor_clientes = conn_clientes.cursor()

# Conexión a la base de datos Productos.db
conn_productos = sqlite3.connect('Datasets/Productos.db')
cursor_productos = conn_productos.cursor()

# Función para obtener un cliente aleatorio
def obtener_cliente_aleatorio():
    cursor_clientes.execute("SELECT Cliente, Comuna, Direccion, Email FROM Clientes ORDER BY RANDOM() LIMIT 1;")
    return cursor_clientes.fetchone()

# Función para obtener un producto aleatorio
def obtener_producto_aleatorio():
    cursor_productos.execute("SELECT Producto, Precio FROM Productos ORDER BY RANDOM() LIMIT 1;")
    return cursor_productos.fetchone()

# Función para generar una transacción aleatoria
def generar_compra():
    cliente = obtener_cliente_aleatorio()
    producto = obtener_producto_aleatorio()

    compra = {
        'Cliente': cliente[0],  # Nombre del cliente
        'Producto': producto[0],        # Nombre del producto
        'Precio': producto[1],           # Precio del producto
        'Pasarela_pago': random.choice(pasarela_pago),
        'Marca_tarjeta': random.choice(marca_tarjeta),
        'Banco': random.choice(banco),
        'Comuna': cliente[1],
        'Direccion': cliente[2],
        'Email': cliente[3],  # Correo del cliente
    }
    return compra

# Función para enviar la compra al servidor gRPC
def enviar_compra(compra):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pedido_pb2_grpc.GestionPedidosStub(channel)
        respuesta = stub.RealizarCompra(pedido_pb2.Compra(
            cliente=compra['Cliente'],
            producto=compra['Producto'],
            precio=compra['Precio'],
            pasarela_pago=compra['Pasarela_pago'],
            marca_tarjeta=compra['Marca_tarjeta'],
            banco=compra['Banco'],
            comuna=compra['Comuna'],
            direccion=compra['Direccion'],
            email=compra['Email']
        ))
        print(respuesta.mensaje)

# Genera una compra aleatoria
compra_aleatoria = generar_compra()

# Muestra la compra generada
print(f'  {compra_aleatoria}\n')

# Enviar la compra al servidor gRPC
enviar_compra(compra_aleatoria)

# Cerrar conexiones
conn_clientes.close()
conn_productos.close()