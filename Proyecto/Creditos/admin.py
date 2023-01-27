from django.contrib import admin
from Creditos.models import Deudores

class DeudoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'deuda_inicial', 'intereses_mensuales')

admin.site.register(Deudores, DeudoresAdmin)
