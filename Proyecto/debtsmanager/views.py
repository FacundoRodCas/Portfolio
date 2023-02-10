from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
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
            valor = round(valor, 2)
            list.append(valor)
        return render(request, 'creditos.html', {'deudores': deudores, 'list': list, 'dolar': dolar_blue})

def crear_deudor(request):
    usuario = get_object_or_404(User, pk = request.user.pk)
    if request.method == 'POST':
        deuda_inicial = request.POST['deuda_inicial']
        form = DeudoresForm(request.POST)
        if form.is_valid():
            deudor = form.save(commit=False)
            deudor.acreedor = usuario
            deudor.deuda_inicial_en_dolares = float(deuda_inicial) / dolar_blue
            deudor.created_at = date.today()
            form.save()
            return redirect('debtsmanager:creditos')
    else:
        form = DeudoresForm()
    return render(request, 'formulario.html', {'form': form})

def modificar_deuda(request, pk):
    deuda = Deudores.objects.get(pk = pk)
    if request.method == 'POST':
        form = DeudoresForm(request.POST, instance=deuda)
        if form.is_valid():
            form.save()
            return redirect('debtsmanager:creditos')
    else:
        form = DeudoresForm(instance=deuda)
    return render(request, 'editar.html', {'form':form})

def eliminar_deuda(request, pk):
    deuda = Deudores.objects.get(pk = pk)
    deuda.delete()
    return redirect('debtsmanager:creditos')