from django.shortcuts import get_object_or_404, render, redirect
from .models import Deudores
from .forms import DeudoresForm
from datetime import date
from django.contrib.auth.models import User
import json
import urllib.request
from datetime import date


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
        form = DeudoresForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.acreedor = request.User
            post.deuda_inicial_en_dolares = form.deuda_inicial * dolar_blue
            post.created_at = date.today()
            post.save()
            return redirect(request, 'creditos.html')
    else:
        form = DeudoresForm()

    return render(request, 'formulario.html', {'form': form})
