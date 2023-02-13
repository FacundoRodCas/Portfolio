Este es el primer proyecto de mi portfolio. En él, creo una página web a través de Django que servirá para crear una cuenta y subir créditos en pesos argentinos. Es una aplicación útil para llevar un registro actualizado de nuestros créditos en pesos.
En el perfil del usuario, se despliegan los créditos actualizados con los intereses mensuales y el precio promedio del dolar blue tal como figura en el documento JSON, en https://api.bluelytics.com.ar/v2/latest.

Para correr la webapp, hará falta:
1) Descargar Python e instalarlo
2) Descargar este repositorio
3) Desde la terminal, entrar a la carpeta del proyecto
4) En la siguiente línea, colocar "pip install Django" (instala django)
5) Descargar e instalar PostgreSQL 
6) Luego, en la terminal, en el directorio de nuestro proyecto, colocar "pip install psycopg2" (instala la librería que permitirá usar PostgreSQL) 
7) Abrir pgAdmin, hacer click derecho en postgres y seleccionar Query tools
8) Si en pgAdmin se colocó una contraseña distinta a "admin", colocar esa contraseña en la variable password en settings.py, en DATABASES (de lo contrario no tocar)
9) Crear una base de datos llamada "Deudores" con el comando "create database Deudroes" y guardarla.
10) En la terminal, en el directorio de la carpeta del proyecto, colocar "pip install psycopg2"
11) En ese mismo directorio, colocar "python manage.py makemigrations"
12) En la siguiente línea, colocar "python manage.py migrate"
13) En la siguiente línea, colocar "python manage.py runserver"
14) Acceder en el navegador, en la barra de direcciones, colocar: 127.0.0.1:8000/home/ y listo.

El proyecto es escalable y próximamente subiré precios históricos del dolar (ya que actualmente solo funciona con el precio actual), además requiere una página 404.
Por último, solo se ha trabajdo en master, ya que no he programado en equipo y el proyecto es relativamente chico.
