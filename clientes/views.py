from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from clientes.models import Cliente, Proyecto
# Create your views here.

## Genero dos contextos para poder dividir en dos div con dos ul el contenido de la consulta.. 
# (Tengo que buscar la fomra de automatizar esto para cuando tenga mas registros en la db)
def experiencia(request):
    clientes=Cliente.objects.all()[:12]
    clientes1=Cliente.objects.all()[12:25]
    return render(request, "clientes/experiencia.html", {"clientes": clientes ,"clientes1": clientes1})


def proyecto(request):
    proyectos=Proyecto.objects.all()
    proyectosAeropuerto=Proyecto.objects.filter(tipo_proyecto="Aeropuertos")
    proyectosViales=Proyecto.objects.filter(tipo_proyecto="CARRETERAS Y VIALIDADES")  
    return render(request, "clientes/proyectos.html", {"proyectos": proyectos, "proyectosAeropuerto":proyectosAeropuerto, "proyectosViales":proyectosViales})

