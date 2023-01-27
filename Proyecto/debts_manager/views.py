from django.shortcuts import render
from debts_manager.admin import DeudoresAdmin
from .models import Deudores
import json
import urllib.request


def mostrar_deudores(request):
    if request.method == 'GET':
        deudores = Deudores.objects.all()
        response = urllib.request.urlopen('https://api.bluelytics.com.ar/v2/latest')
        response_body = response.read()
        response_json = json.loads(response_body.decode('utf-8'))
        dolar_blue = response_json.get('blue')['value_avg']
        

        return render(request, 'creditos.html', {'deudores': deudores})
