from django.shortcuts import render, redirect
from .models import Deudores
import json
import urllib.request
from datetime import date
from .forms import DeudoresForm
from datetime import date
from django.contrib.auth.models import User

response = urllib.request.urlopen('https://api.bluelytics.com.ar/v2/latest')
response_body = response.read()
json_response = json.loads(response_body.decode('utf-8'))
dolar_blue = float(json_response.get('blue')['value_avg'])


def mostrar_deudores(request):
    if request.method == 'GET':
        deudores = Deudores.objects.filter(acreedor = request.user)
        today = date.today()
        list = []
        for deudor in deudores:
            meses_pasados = ((today.year - deudor.created_at.year) * 12) + (today.month - deudor.created_at.month)
            intereses_totales = ((deudor.deuda_inicial_en_dolares / 100) * deudor.intereses_mensuales)
            valor = (deudor.deuda_inicial_en_dolares + (meses_pasados * intereses_totales)) * dolar_blue
            list.append(valor)
        return render(request, 'creditos.html', {'deudores': deudores, 'list': list, 'dolar': dolar_blue})

def crear_deudor(request):
    if request.method == 'POST':
        form=DeudoresForm(request.POST)
        if form.is_valid():
            deudor = Deudores.objects.create(nombre = form['nombre'],
                            apellido = form['apellido'],
                            deuda_inicial = form['deuda_inicial'],
                            deuda_inicial_en_dolares = dolar_blue,
                            intereses_mensuales = form['intereses_mensuales'],
                            created_at = date.today()
                            )
            return redirect(request, '/gracias.html/')
    else:
        form = DeudoresForm()

    return render(request, 'formulario.html', {'form': form})

       #FALTA EL USUARIO

