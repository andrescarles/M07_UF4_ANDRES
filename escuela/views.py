from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
template = loader.get_template('index.html')

def index(request):
    return HttpResponse(template.render())

def alumns(request):
    context = {
        "data" : [{"name":"Moises", "surname":"Chukiruna",},{"name":"Marc", "surname":"Soler",},{"name":"Marc", "surname":"Salas",}],
    }
    return HttpResponse(template.render(context, request))

def profes(request):
    context = {
        "data" : [{"name":"Roger", "surname":"Sobrino",},{"name":"Juan", "surname":"Dolores",},{"name":"Pepe", "surname":"Montoya",}],
    }
    return HttpResponse(template.render(context))