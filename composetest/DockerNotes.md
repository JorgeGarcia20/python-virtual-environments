# ¿Qué es un Dockerfile?
Un archivo `Dockerfile` es un documento de texto que contiene todos los comandos que un usuario podria ejecutar en una linea de comandos o terminal para ensamblar una imagen de docker.
Docker puede construir imagenes automaticamente leyendo las instrucciones en un `Dockerfile`.

# Formato
Los `Dockerfile` tienen un formato para establecer las instrucciones a seguir.

```sh
INSTRUCTION argument
```

Las instrucciones no son case-sensitive, pero, por convencion es mejor definir las instrucciones en mayúscular y los argumentos en minúsculas.

Para saber mas acerca de [Dockerfiles](https://docs.docker.com/engine/reference/builder/ "Dockerfile reference").

# Ejemplo de un Dockerfile
```Dockerfile
# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]
```

Este `dockerfile` le dice a docker que:
1. Construir una imagen, en este caso la imagen de `python 3.7`.
2. Establecer el directorio de trabajo (Working directory) a `/code`.
3. Establecer variables de entorno, en este caso usando `flask`.
4. Instalar `gcc` y otras dependencias.
5. Copiar el archivo `requirements.txt` a un archivo en el Working directory con el mismo nombre.
6. Instalar las librerias con el comando `pip install -r <file>`.
7. Indicar que el contenedor debe escuchar en el puerto `5000`.
8. Copiar el directorio actual `.` al working directory `.` en la imagen.
9. Establecer el comando predeterminado del contenedor a `flask run`.

# Docker compose
`Compose` es una herramienta para definir y correr aplicaciones docker multicontenedor. Con `compose` se usa un archivo `YALM` para configurar servicios de aplicación. Despues con un solo comando es posible crear e iniciar todos los servicios de su configuración.

`Compose` funciona en todos los entornos: produccion, staging, desarrollo, testing incluso flujos de trabajo CI.
* Inicia, detiene y recrea servicios.
* Ver el estado de los servicios en ejecución.
* Transmita la salida de registros de los servicios en ejecución
* Ejecutar un comando único en un servicio.

las caracteristicas clave de `compose` que lo hacen efectivo son:
* Tener multiples entornos aislados en un solo host.
* Conserva los datos de volumen cuando se crean contenedores.
* Solo recrea contenedores que han cambiado.
* Admite variables y mover una composición entre entornos.

```yml
version: "3.9"
services:
  web:
    build: .
    ports:
      - "8000:5000"
  redis:
    image: "redis:alpine"
```
Este archivo `compose` define dos servicios: `web` y `redis`.
El servicio `web` usa una imagen que es construida desde el `Dockerfile` en el directorio actual. Este despues une el contenedor y el host de la maquina para exponer el puerto `8000`. Este ejemplo usa el puerto `5000` para el servidor web de `Flask`.
El servicio `redis` usa una imagen publica de obtenida del registro de Docker Hub.

# Costruye y corre una aplicación con `Compose`
Desde el directorio del projecto se debe ejecutar el siguiente comando para poner en marcha la aplicación.
```sh
docker compose up
```