from django.shortcuts import render, redirect
from contacto.models import Contacto
from clientes.models import Cliente, Proyecto
from .forms import ClienteForm, ProyectosForm, UserRegistrationForm 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
 

#CRUD CLIENTES
@login_required
def list_client(request):
   busquedas = request.GET.get('buscar')
   busquedasProyectos = request.GET.get('buscarproyectos')
   clientes = Cliente.objects.get_queryset().order_by('-id')
   mensajes = Contacto.objects.get_queryset().order_by('-id')
   paginator = Paginator(clientes, 8)
   page = request.GET.get('page1')

   try: 
       clientes = paginator.page(page)
   except PageNotAnInteger:
       clientes = paginator.page(1)  
   except EmptyPage:
       clientes = paginator.page(paginator.num_pages)

   if  busquedas:
       clientes = Cliente.objects.filter(
           Q(nombre_cliente__icontains = busquedas)
       ).distinct
    
   proyectos = Proyecto.objects.get_queryset().order_by('-year') #acomodo por fechas
   paginator = Paginator(proyectos, 5) 
   page = request.GET.get('page2') 
  
   
   try: 
       proyectos = paginator.page(page)
   except PageNotAnInteger:
       proyectos = paginator.page(1)  
   except EmptyPage:
       proyectos = paginator.page(paginator.num_pages)
       
   if  busquedasProyectos:
        proyectos = Proyecto.objects.filter(
        Q(nombre_proyecto__icontains = busquedasProyectos)|
        Q(tipo_proyecto__icontains = busquedasProyectos) |
        Q(year__icontains = busquedasProyectos)| 
        Q(created__icontains = busquedasProyectos) |
        Q(clientes__nombre_cliente__icontains = busquedasProyectos) #Especifico que campo quiero del nanytonany
       ).distinct 
    

     
    
   return render(request, 'admcatsa/admcatsa.html', {'clientes': clientes ,'proyectos': proyectos, 'mensajes':mensajes,})



@login_required
def create_cliente(request):
    form = ClienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_client')
    return render(request, 'admcatsa/admcatsa-form.html', {'form': form}) 

@login_required
def create_proyecto(request):
    formProyecto = ProyectosForm(request.POST, request.FILES)

    if formProyecto.is_valid():
        formProyecto.save()
        return redirect('list_client')
    
    
    return render(request, 'admcatsa/admcatsa-form-proyecto.html', {'formProyecto': formProyecto }) 
@login_required
def update_cliente(request, id):
    clientes =  Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=clientes)
    if form.is_valid():
       form.save()
       return redirect('list_client')
    
    return render(request, 'admcatsa/admcatsa-form.html', {'form': form ,'clientes': clientes }) 


@login_required
def update_proyecto(request, id):
    proyectos = Proyecto.objects.get(id=id)
    formProyecto = ProyectosForm(request.POST or None, instance=proyectos) 
    
    if formProyecto.is_valid():
       formProyecto.save()
       return redirect('list_client')
    return render(request, 'admcatsa/admcatsa-form-proyecto.html', {'formProyecto': formProyecto , 'proyectos':proyectos }) 
    
        
@login_required
def delete_cliente(request, id):
    clientes =  Cliente.objects.get(id=id)
    if request.method=="POST":
        clientes.delete()
        return redirect('list_client')
    

    return render(request, 'admcatsa/admcatsa-delete-confirm.html', {'clientes': clientes, }) 

@login_required
def delete_proyecto(request, id):
    proyectos =  Proyecto.objects.get(id=id)
    if request.method=="POST":
        proyectos.delete()
        return redirect('list_client')
    
    return render(request, 'admcatsa/admcatsa-delete-confirm-proyecto.html', {'proyectos': proyectos})

@login_required
def list_mensajes(request):
   busquedas = request.GET.get('buscar')
   mensajes = Contacto.objects.get_queryset().order_by('-id')
   paginator = Paginator(mensajes, 5)
   page = request.GET.get('page')
   print(mensajes) 
   try: 
       mensajes = paginator.page(page)
   except PageNotAnInteger:
       mensajes = paginator.page(1)  
   except EmptyPage:
       mensajes = paginator.page(paginator.num_pages)
       
   if  busquedas:
       mensajes = Contacto.objects.filter(
           Q( Nombre__icontains= busquedas)| 
           Q( Apellido__icontains= busquedas)|
           Q( Asunto__icontains= busquedas)|
           Q( Email__icontains= busquedas)|
           Q( Telefono__icontains= busquedas)|
           Q( created_at__icontains= busquedas)|
           Q( Mensaje__icontains= busquedas) 
       ).distinct
   return render(request, 'admcatsa/mensajes.html', {'mensajes': mensajes })
@login_required
def delete_mensaje(request, id):
    deleteMensaje = Contacto.objects.get(id=id)
    if request.method=="POST":
        deleteMensaje.delete()
        return redirect('list_mensajes')
    return render(request, 'admcatsa/admcatsa-delete-confirm-mensaje.html', {'deleteMensaje': deleteMensaje })  
@login_required
def register(request):
    if request.method=="POST":
       form =  UserRegistrationForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data['username']
           messages.success(request, f'Usuario {username} creado')
    else:
        form =  UserRegistrationForm()        
    context=  {'form' : form}     
    return render(request, 'admcatsa/register.html', context)