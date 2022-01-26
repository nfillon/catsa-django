from django.shortcuts import render
from clientes.models import Cliente
# Create your views here.


def home(request):
    return render(request, "Catsaweb/index.html")

def insfrastructura(request):
    return render(request, "Catsaweb/infrastructura.html")

def experiencia(request):
    return render(request, "Catsaweb/experiencia.html")

def proyecto(request):
    proyectos=Cliente.objects.all()
    return render(request, "Catsaweb/proyectos.html", {"proyectos": proyectos})

def conctacto(request):
    return render(request, "contacto/contacto.html")

# def admcatsa(request):
#      return render(request, "admcatsa/admcatsa.html")