Este es el primer proyecto de mi portfolio. En él, creo una página web a través de Django que servirá para crear una cuenta y subir créditos en pesos argentinos.
En el perfil del usuario se despliegan los créditos actualizados con el precio promedio del dolar blue que figura en el documento JSON, en https://api.bluelytics.com.ar/v2/latest.

Para correr la webapp, hará falta:
1) Instalar y descargar Python
2) Descargar este proyecto
3) Buscar la carpeta "Proyecto", donde se encuentra el archivo "manage.py" y copiar el directorio
4) En la terminal, escribir el comando "cd" y pegar el directorio copiado
5) En la siguiente línea, colocar "pip install Django" (instalamos django)
6) Descargamos PostgreSQL y los instalamos
7) Luego, en la terminal, en el directorio donde se encuentra manage.py, colocamos "pip install psycopg2" (instalamos la librería que nos permitirá usar PostgreSQL) 
8) Abrir pgAdmin, hacer click derecho en postgres y seleccionar Query tools
9) Si en pgAdmin se colocó una contraseña distinta a "admin", colocar esa contraseña en la variable password en settings.py. en DATABASES (de lo contrario no tocar)
10) Crear una base de datos llamada "Deudores" con el comando "create database Deudroes" y guardarla.
11) En la terminal, en el directorio de la carpeta de nuestro proyecto, colocar "pip install psycopg2"
12) En ese mismo directorio, colocar "python manage.py makemigrations"
13) En la siguiente línea, colocar "python manage.py migrate"
14) En la siguiente línea, colocar "python manage.py runserver"
15) Acceder en el navegador, en la barra de direcciones, colocar: 127.0.0.1:8000/home/ y listo.

El proyecto es escalable y proximamente subiré precios históricos del dolar (ya que actualmente solo funciona con el precio actual), además requiere una página 404.
