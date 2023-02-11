#La app Registro sirve paramanejar sesiones y registro de nuevos usuarios
#Importamos login, authenticate y logout.
from django.contrib.auth import login, authenticate, logout
#Importamos los shortcuts de render y redirect.
from django.shortcuts import redirect, render
#Importamos los formularios genéricos para la creación de usuario y autenticación.
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#Importamos View para establecer una class-based view.
from django.views.generic import View
#Importamos messages para comunicar al usuario posibles errores.
from django.contrib import messages

#Definimos la clase de la view del registro con dos métodos (get y post) diferenciados por funciones.
class Registro(View):
    #Desplegamos el formulario de registro.
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro.html', {'form': form})
    #Definimos el método POST que nos permite guardar la información enviada por el usuario.
    def post(self, request):
        form = UserCreationForm(request.POST)
        #Preguntamos si la información enviada es válida.
        if form.is_valid():
            #Si es válida, guardamos el usuario, hacemos login y redirigimos al home.
            usuario = form.save()
            login(request, usuario)
            return redirect('home')
        else:
            #Si no es válida, informamos del error.
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
        return render(request, 'home.html', {'form': form})

#Definimos la función de cerrar sesión que redirige al home.
def cerrar_sesion(request):
    logout(request)
    return redirect('home')

#Definimos la función de login.
def iniciar_sesion(request):
    #Si el método del request es "POST", y la información es válida, guardamos esa información.
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            #Definimos los valores de las variables de username y password a partir de la información enviada por el usuario.
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #Autenticamos al usuario a partir de las variables username y password.
            user = authenticate(request, username=username, password=password)
            #Si el valor del usuario no es None, se hace login y se redirige al home.
            if user is not None:
                login(request, user)
                return redirect('home')
            #Sino, se envía un mensaje del error.
            else:
                messages.success(request, ('Hubo un error, inténtalo de nuevo.'))
                return redirect('login.html')
    #Desplegamos el formulario genérico de autenticación.
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})