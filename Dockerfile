# Usa una imagen base de Python
FROM python:3.12

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Expone el puerto 8000 para que pueda ser accesible desde fuera del contenedor
EXPOSE 8000
# Ejecuta el comando de entrada para iniciar el servidor
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
