from django.db import models

class Deudores(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    deuda_inicial = models.FloatField()
    intereses_mensuales = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

