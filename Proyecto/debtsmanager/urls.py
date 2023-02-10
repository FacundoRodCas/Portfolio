from django.urls import path
from .views import mostrar_deudores, crear_deudor, modificar_deuda, eliminar_deuda



app_name = 'debtsmanager'
urlpatterns = [
    path('creditos/', mostrar_deudores, name = 'creditos'),
    path('formulario/', crear_deudor, name = 'formulario'),
    path('gracias/', crear_deudor, name = 'gracias'),
    path('editar/<int:pk>', modificar_deuda, name='modificar'),
    path('eliminar/<int:pk>', eliminar_deuda, name = 'eliminar')
    
]
