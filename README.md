# Maullidos

Aplicación para postear mensajes "Maullidos".
## Instalación y Ejecución

### Con Docker

1. **Requisitos previos**:
   - Docker instalado en tu sistema.

2. **Clona el repositorio**:
   ```bash
   git clone https://github.com/JuanFalHqz/Maullidos.git
3. **Construye la imagen**:
   
   En este caso la imagen se puede llamar maullidos.
   ```bash
   docker build -t maullidos .
4. **Ejecuta el contenedor**:
   ```bash
   docker run -d -p 8000:8000 maullidos 

5. **Haz las migraciones**:
   6. Revisa el id de la imagen:
      ```bash
      docker ps
   7. Crea las migraciones:
      ```bash
      docker exec <ID_DEL_CONTENEDOR> python manage.py makemigrations
   8. Aplicar las migraciones:
      ```bash
      docker exec <ID_DEL_CONTENEDOR> python manage.py migrate

La aplicación estará disponible en http://localhost:8000.

**Saludos**
