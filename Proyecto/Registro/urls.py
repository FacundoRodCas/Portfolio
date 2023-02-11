from django.urls import path
#Importamos las vistas del módulo views de la app.
from .views import Registro, iniciar_sesion, cerrar_sesion

#Definimos el nombre de la app para poder hacer los redirects con mayor facilidad.
app_name='registro'
#Definimos los path de la app.
urlpatterns = [
    path('', Registro.as_view(), name='registrarse'),
    path('login/', iniciar_sesion, name= 'iniciar_sesion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion')
]
