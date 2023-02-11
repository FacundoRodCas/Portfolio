from django.urls import path
#Importamos las views del módulo views de esta app.
from .views import mostrar_deudores, crear_deudor, modificar_deuda, eliminar_deuda


#Nombramos la app.
app_name = 'debtsmanager'
#Definimos los path de esta app.
urlpatterns = [
    path('creditos/', mostrar_deudores, name = 'creditos'),
    path('formulario/', crear_deudor, name = 'formulario'),
    path('gracias/', crear_deudor, name = 'gracias'),
    path('editar/<int:pk>', modificar_deuda, name='modificar'),
    path('eliminar/<int:pk>', eliminar_deuda, name = 'eliminar')
    
]
