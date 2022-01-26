from django.http import HttpResponse
from django.shortcuts import render
from .models import Contacto

# Create your views here.

def conctactoWeb(request):
    if request.method=="POST":
        contacto=Contacto()
        Nombre=request.POST.get('Nombre')
        Apellido=request.POST.get('Apellido') 
        Email=request.POST.get('Email') 
        Telefono=request.POST.get('Telefono')
        Asunto=request.POST.get('Asunto')
        Mensaje=request.POST.get('Mensaje')
        contacto.Nombre=Nombre
        contacto.Apellido=Apellido
        contacto.Email=Email
        contacto.Telefono=Telefono
        contacto.Asunto=Asunto
        contacto.Mensaje=Mensaje
        contacto.save()
        return HttpResponse("<h1>Gracias Por Contactarnos</h1>") 
    return render(request, "contacto/contacto.html")