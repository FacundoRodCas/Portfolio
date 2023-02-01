from django.contrib import admin
from .models import Deudores

class DeudoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'deuda_inicial', 'deuda_inicial_en_dolares', 'intereses_mensuales', 'acreedor', 'created_at')


admin.site.register(Deudores, DeudoresAdmin)
