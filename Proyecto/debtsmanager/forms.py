from django import forms


class DeudoresForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    deuda_inicial = forms.FloatField()
    intereses_mensuales = forms.IntegerField()
    