#Importamos los shortcuts.
from django.shortcuts import get_object_or_404, render, redirect
#Importamos el model Deudores del módulo models de esta app.
from .models import Deudores
#Importamos el ModelForm DeudoresForm correlativa al model Deudores.
from .forms import DeudoresForm
#Importamos fecha.
from datetime import date
#Importamos User.
from django.contrib.auth.models import User
#Importamos json y urllib.request para obtener el precio promedio del dolar blue
import json
import urllib.request


#En este bloque de código abrimos el archivo JSON, lo leemos, lo decodificamos, lo pasamos a diccionario.
response = urllib.request.urlopen('https://api.bluelytics.com.ar/v2/latest')
response_body = response.read()
json_response = json.loads(response_body.decode('utf-8'))
#Recuperamos el valor promedio del dolar blue y lo pasamos a float.
dolar_blue = float(json_response.get('blue')['value_avg'])

#Definimos la función que muestra nuestros créditos.
def mostrar_deudores(request):
    #Si el método es "GET", filtramos los objetos cuyo atributo acreedor sea igual al usuario del request.
    if request.method == 'GET':
        deudores = Deudores.objects.filter(acreedor = request.user)
        #definimos la variable today con el valor de la fecha actual.
        today = date.today()
        #Creamos una lista vacía.
        list = []
        '''Por cada uno de los objetos filtrados, llevamos a cabo una operación que nos permite actualizar
         la deuda en pesos argentinos.'''
        for deudor in deudores:
            #Se cuentan cuántos meses han pasado desde la creación de la deuda.
            meses_pasados = ((today.year - deudor.created_at.year) * 12) + (today.month - deudor.created_at.month)
            #Se calcula el interes mensual en dolares.
            intereses_totales = ((deudor.deuda_inicial_en_dolares / 100) * deudor.intereses_mensuales)
            '''Se suma la deuda inicial en dolares con el total de los intereses en dolares
             y se lo multiplica por el precio del dolar blue, lo que da el total de la deuda en pesos argentinos'''
            valor = (deudor.deuda_inicial_en_dolares + (meses_pasados * intereses_totales)) * dolar_blue
            #Limitamos la cantidad de decimales del float a dos.
            valor = round(valor, 2)
            #Agregamos ese valor a la lista vacía de esta función.
            list.append(valor)
            #Mostramos cada uno de los objetos filtrados, la lista y el precio actual del dolar blue
        return render(request, 'creditos.html', {'deudores': deudores, 'list': list, 'dolar': dolar_blue})

#Definimos la función crear_deudor.
def crear_deudor(request):
    #Definimos una variable usuario a partir del primary key del usuario que hace el request.
    usuario = get_object_or_404(User, pk = request.user.pk) #Todavía no hemos programado la pág 404.
    #Si el método del request es "POST", creamos el objeto.
    if request.method == 'POST':
        #Definimos la variable deuda_inicial con el valor de deuda_inicial enviada por el usuario.
        deuda_inicial = request.POST['deuda_inicial']
        #Creamos el objeto form a partir del formuario DeudoresForm y la información enviada por el usuario.
        form = DeudoresForm(request.POST)
        '''Si la información es válida, guardamos, pero todavía no hacemos commit, puesto que hará falta
        que se rellenen otros campos del ModelDeudores automaticamente.'''
        if form.is_valid():
            deudor = form.save(commit=False)
            #Definimos el campo acreedor a partir de la variable usuario definida anteriormente.
            deudor.acreedor = usuario
            #Definimos la deuda inicial en dolares multiplicando la variable deuda inicial por el precio del dolar blue
            deudor.deuda_inicial_en_dolares = float(deuda_inicial) / dolar_blue
            #Definimos la fecha de creación de la deuda de manera automática.
            deudor.created_at = date.today()
            #Ahora sí, guardamos el objeto.
            form.save()
            #Redirigimos al perfil del usuario.
            return redirect('debtsmanager:creditos')
    #Si el método no es "POST", desplegamos el formulario DeudoresForm.
    else:
        form = DeudoresForm()
    return render(request, 'formulario.html', {'form': form})

#Definimos la función modificar_deuda que recibe como parámetro la primary key de la deuda a modificar.
def modificar_deuda(request, pk):
    #Obtenemos el objeto que será modificado a partir de la primary key y se lo asignamos a la variable deuda.
    deuda = Deudores.objects.get(pk = pk)
    #Si el método del request es "POST", se recupera la información enviada por el usuario.
    if request.method == 'POST':
        form = DeudoresForm(request.POST, instance=deuda)
        #Si la información es válida, guardamos el objeto.
        if form.is_valid():
            form.save()
            #redirigimos al perfil del usuario.
            return redirect('debtsmanager:creditos')
    #Si el método no es post, desplegamos el formulario DeudroesForm.
    else:
        form = DeudoresForm(instance=deuda)
    return render(request, 'editar.html', {'form':form})

#Definimos la view eliminar_deuda, obtenemos la primary key de la deuda en cuestión como parámetro.
def eliminar_deuda(request, pk):
    #Obtenemos la deuda en cuestión a partir de la primary key
    deuda = Deudores.objects.get(pk = pk)
    #Borramos el objeto de la base de datos.
    deuda.delete()
    #Redirigimos al perfil
    return redirect('debtsmanager:creditos')