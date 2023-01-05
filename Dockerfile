FROM python:3

# Copiamos el archivo .env al contenedor
COPY .env /app/.env

# Instalamos la biblioteca de Discord y python-dotenv
RUN pip install discord python-dotenv

# Copiamos nuestro script en el contenedor
COPY main.py /app/main.py

# Establecemos el script como el archivo de entrada principal
ENTRYPOINT ["python", "/app/main.py"]
