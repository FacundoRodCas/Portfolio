from django.urls import path
from .views import Registro, iniciar_sesion, cerrar_sesion

app_name='registro'
urlpatterns = [
    path('', Registro.as_view(), name='registrarse'),
    path('login/', iniciar_sesion, name= 'iniciar_sesion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion')
]
