
from itertools import product
from django.shortcuts import render, redirect
from clientes.models import Cliente, Proyecto
from .forms import ClienteForm, ProyectosForm


#CRUD CLIENTES
def list_client(request):
   clientes = Cliente.objects.all()
   proyectos = Proyecto.objects.all()
   print(clientes)
   return render(request, 'admcatsa/admcatsa.html', {'clientes': clientes, 'proyectos': proyectos})
   

def create_cliente(request):
    form = ClienteForm(request.POST or None)
    formProyecto = ProyectosForm(request.POST or None)
        
    if form.is_valid():
        form.save()
        return redirect('list_client')
    
    if formProyecto.is_valid():
        formProyecto.save()
        return redirect('list_client')
    
    
    return render(request, 'admcatsa/admcatsa-form.html', {'form': form, 'formProyecto': formProyecto }) 

def update_cliente(request, id):
    clientes =  Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=clientes)
    if form.is_valid():
       form.save()
       return redirect('list_client')
    
    return render(request, 'admcatsa/admcatsa-form.html', {'form': form ,'clientes': clientes }) 



def update_proyecto(request, id):
    proyectos = Proyecto.objects.get(id=id)
    formProyecto = ProyectosForm(request.POST or None, instance=proyectos) 
    
    if formProyecto.is_valid():
       formProyecto.save()
       return redirect('list_client')
    return render(request, 'admcatsa/admcatsa-form-proyecto.html', {'formProyecto': formProyecto , 'proyectos':proyectos }) 
    
        
    
def delete_cliente(request, id):
    clientes =  Cliente.objects.get(id=id)
    if request.method=="POST":
        clientes.delete()
        return redirect('list_client')
    

    return render(request, 'admcatsa/admcatsa-delete-confirm.html', {'clientes': clientes, }) 

def delete_proyecto(request, id):
    proyectos =  Proyecto.objects.get(id=id)
    if request.method=="POST":
        proyectos.delete()
        return redirect('list_client')
    
    return render(request, 'admcatsa/admcatsa-delete-confirm-proyecto.html', {'proyectos': proyectos}) 