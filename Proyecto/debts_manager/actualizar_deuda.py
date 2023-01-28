import json
import urllib.request

response = urllib.request.urlopen('https://api.bluelytics.com.ar/v2/latest')
response_body = response.read()
json_response = json.loads(response_body.decode('utf-8'))
dolar_blue = float(json_response.get('blue')['value_avg'])