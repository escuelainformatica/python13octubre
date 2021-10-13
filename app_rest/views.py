import json
import requests
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def mivista(request:WSGIRequest ):
    dic=json.loads(request.body.decode('utf-8'))
    sumar=dic['num1']+dic['num2']

    return JsonResponse({"resultado":sumar})

def clienteweather(request):
    datos={'q':'Santiago','appid':'xxxxx'}  #todo: falta el codigo
    r=requests.get('https://api.openweathermap.org/data/2.5/weather',params=datos)
    dic = json.loads(r.content)
    return JsonResponse(dic)


def clientevista(request):
    datos = {
        "num1": 1,
        "num2": 2
    }

    r = requests.post('http://127.0.0.1:8000/test/', json=datos,headers={})
    dic=json.loads(r.content)
    return render(request,"resultado.html",dic)

def clientedolar(request):
    r=requests.get('https://mindicador.cl/api/dolar')
    dic = json.loads(r.content)
    return render(request, "dolar.html", dic)


