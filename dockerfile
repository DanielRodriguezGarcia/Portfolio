# Usar una imagen base de Python
FROM python:3.12

# Establecer el directorio de trabajo
WORKDIR /portfolio-asir

# Copiar los archivos del proyecto
COPY . .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto 5000
EXPOSE 5000

#Comando para correr la app con gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]