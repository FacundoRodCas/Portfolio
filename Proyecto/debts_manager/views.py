from django.shortcuts import render
from .models import Deudores
import json
import urllib.request
from datetime import date


def mostrar_deudores(request):
    if request.method == 'GET':
        deudores = Deudores.objects.filter(acreedor = request.user)
        response = urllib.request.urlopen('https://api.bluelytics.com.ar/v2/latest')
        response_body = response.read()
        json_response = json.loads(response_body.decode('utf-8'))
        dolar_blue = float(json_response.get('blue')['value_avg'])
        today = date.today()
        list = []
        for deudor in deudores:
            list.append((deudor.deuda_inicial_en_dolares * dolar_blue) + (((((today.year -deudor.created_at.year) * 12) + (today.month - deudor.created_at.month)) * ((deudor.deuda_inicial_en_dolares / 100) * deudor.intereses_mensuales))) * dolar_blue)
        return render(request, 'creditos.html', {'deudores': deudores, 'list': list, 'dolar': dolar_blue})

