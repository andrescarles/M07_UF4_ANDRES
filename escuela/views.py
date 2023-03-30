from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

def index(request):
    return render(request,'index.html')

def alumns(request):
    
    context = {
        "data" : [{"name":"Moises", "surname":"Chukiruna",},{"name":"Marc", "surname":"Soler",},{"name":"Marc", "surname":"Salas",}],
    }
    return render(request,'alumnes.html',context)

def alumns2(request, nombre):
    one = {"data":[]}
    context = {"data":[{"name":"Moises", "surname":"Chukiruna",},{"name":"Marc", "surname":"Soler",},{"name":"Marco", "surname":"Salas",}]}
    
    for i in context["data"]:
       if i["name"] == nombre:
        one["data"].append(i)

    return render(request,'alumnes.html',one)

def profes(request):
    context = {
        "data" : [{"name":"Roger", "surname":"Sobrino",},{"name":"Juan", "surname":"Dolores",},{"name":"Pepe", "surname":"Montoya",}],
    }
    return render(request,'profes.html',context)

def profes2(request, nombre):
    one = {"data":[]}
    context = {"data"[{"name":"Roger", "surname":"Sobrino",},{"name":"Juan", "surname":"Dolores",},{"name":"Pepe", "surname":"Montoya",}]}
    
    for i in context["data"]:
       if i["name"] == nombre:
        one["data"].append(i)

    return render(request,'profes.html',one)
