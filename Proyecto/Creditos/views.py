from django.shortcuts import render
from Creditos.admin import DeudoresAdmin
from .models import Deudores


def mostrar_deudores(request):
    if request.method == 'GET':
        deudores = Deudores.objects.all()
        return render(request, 'creditos.html', {'deudores': deudores})
