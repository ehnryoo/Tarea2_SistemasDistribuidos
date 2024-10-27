# Dockerfile consolidado
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que se ejecutará el servicio gRPC
EXPOSE 50051

# Comando para ejecutar ambos scripts
CMD ["sh", "-c", "python server.py & python generar_compra.py"]

