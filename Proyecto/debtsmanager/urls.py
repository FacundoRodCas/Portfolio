from django.urls import path
from .views import mostrar_deudores, crear_deudor



app_name = 'debtsmanager'
urlpatterns = [
    path('', mostrar_deudores),
    path('formulario/', crear_deudor, name = 'formulario'),
    path('gracias/', crear_deudor, name = 'gracias')
    
]
