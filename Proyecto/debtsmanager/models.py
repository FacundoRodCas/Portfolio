from django.db import models
#Importamos User
from django.contrib.auth.models import User

#Definimos la clase Deudores y sus atributos.
class Deudores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    deuda_inicial = models.FloatField()
    deuda_inicial_en_dolares = models.FloatField(blank=True)
    intereses_mensuales = models.IntegerField()
    acreedor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField()

    