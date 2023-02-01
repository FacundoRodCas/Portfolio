from telnetlib import LOGOUT
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from django.contrib import messages
from debtsmanager.views import dolar_blue


class Registro(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)

            return render('home.html', {{'dolar': dolar_blue}})

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            
            return render(request, 'home.html', {'form': form})

def cerrar_sesion(request):
    LOGOUT(request)
    return redirect('home.html')

def login(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})