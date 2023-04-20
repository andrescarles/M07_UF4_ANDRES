from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader, Context
from .form  import alumno_objeto,profesor_objeto
from .models import alumno,profesor


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
    context = {"data":[{"name":"Roger", "surname":"Sobrino",},{"name":"Juan", "surname":"Dolores",},{"name":"Pepe", "surname":"Montoya",}]}
    
    for i in context["data"]:
       if i["name"] == nombre:
        one["data"].append(i)

    return render(request,'profes.html',one)

def formulario_alumno(request):
    #form = objeto()
    form = alumno_objeto()
    data = [{'name': obj.name, 'surname': obj.surname} for obj in alumno.objects.all()]
    if request.method == 'POST':
        form = alumno_objeto(request.POST)
        if form.is_valid():
            form.save()
            context = {
                "data" : data,
            }
            return render(request,'alumnes.html', context)
    context = {'form':form}
    return render(request,'form.html',context)

def formulario_profe(request):
    #form = objeto()
    form = profesor_objeto()
    data = [{'name': obj.name, 'surname': obj.surname} for obj in profesor.objects.all()]
    if request.method == 'POST':
        form = profesor_objeto(request.POST)
        if form.is_valid():
            form.save()
            
            context = {
                "data" : data,
            }
            return render(request,'profes.html', context)
    context = {'form':form}
    return render(request,'form.html',context)


    
def update_alumno(request, pk):
    #form = objeto()
    query = alumno.objects.get(name = pk)
    data = {'name': query.name, 'surname': query.surname}
    form = alumno_objeto(instance=query)
    if request.method == 'POST':
        form = alumno_objeto(request.POST, instance=query)
        if form.is_valid():
            form.save()
            context = {
                "data" : data,
            }
            return render(request,'alumnes.html', context)
    context = {'form':form}
    return render(request,'form.html',context)

def update_profe(request,pk):
    #form = objeto()
    query = profesor.objects.get(name = pk)
    form = profesor_objeto()
    data = {'name': query.name, 'surname': query.surname}
    if request.method == 'POST':
        form = profesor_objeto(request.POST)
        if form.is_valid():
            form.save()
            context = {
                "data" : data,
            }
            return render(request,'profes.html', context)
    context = {'form':form}
    return render(request,'form.html',context)