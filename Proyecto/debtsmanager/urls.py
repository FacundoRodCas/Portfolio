from django.urls import path
from .views import mostrar_deudores
from .views import crear_deudor


app_name = 'debtsmanager'
urlpatterns = [
    path('', mostrar_deudores),
    path('formulario/', crear_deudor),
    path('gracias/', crear_deudor, name = 'gracias'),
]
