#Importamos el shortcut render.
from django.shortcuts import render
#Importamos json y urllib.request para tomar el precio del dolar actualizado.
import json
import urllib.request

#Vista del home: recupera el pecio del dolar blue y se envía al template para luego ser desplegado.
def home(request):
    response = urllib.request.urlopen('https://api.bluelytics.com.ar/v2/latest')
    response_body = response.read()
    response_json = json.loads(response_body.decode('utf-8'))
    dolar_blue = response_json.get('blue')['value_avg']

    return render(request, 'home.html', {'dolar': dolar_blue})
    