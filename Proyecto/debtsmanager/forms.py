from django import forms
#Importamos el Model Deudores
from .models import Deudores

#Definimos el formulario relativo al Model Deudores.
class DeudoresForm(forms.ModelForm):
    '''Solo definimos cuatro campos, ya que el resto será completado automáticamente de acuerdo a la fecha,
     usuario o precio actual del dolar blue.'''
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    deuda_inicial = forms.FloatField()
    intereses_mensuales = forms.IntegerField()
    class Meta:
        #Establecemos la relación del formulario con el Model Deudores.
        model = Deudores
        #Definimos los campos a mostrar.
        fields = ['nombre', 'apellido', 'deuda_inicial', 'intereses_mensuales']
