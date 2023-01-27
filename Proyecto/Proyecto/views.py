from django.shortcuts import render, redirect
import json
import urllib.request

def home(request):
    response = urllib.request.urlopen('https://api.bluelytics.com.ar/v2/latest')
    response_body = response.read()
    response_json = json.loads(response_body.decode('utf-8'))
    dolar_blue = response_json.get('blue')['value_avg']

    return render(request, 'home.html', {'dolar': dolar_blue})
    