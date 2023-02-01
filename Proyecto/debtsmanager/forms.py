from django import forms
from .models import Deudores

class DeudoresForm(forms.ModelForm):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    deuda_inicial = forms.FloatField()
    intereses_mensuales = forms.IntegerField()
    class Meta:
        model = Deudores
        fields = ['nombre', 'apellido', 'deuda_inicial', 'intereses_mensuales']
