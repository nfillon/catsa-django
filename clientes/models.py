
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
import datetime



class Cliente(models.Model):
    nombre_cliente=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
      
    class Meta:
        verbose_name='cliente'
        verbose_name_plural='clientes'
    
    def __str__(self):
        return self.nombre_cliente
    
    
    
class Proyecto(models.Model):
       #Para tomar solo la propiedad del anio del la fucnion datetime
    YEAR_CHOICES = []
    for r in range(2000, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    tipo_proyecto=models.CharField(max_length=50)  
    nombre_proyecto=models.TextField(max_length=500)
    year = models.IntegerField(choices=YEAR_CHOICES,default=datetime.datetime.now().year)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    clientes=models.ManyToManyField(Cliente)     
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='proyecto'
        verbose_name_plural='proyectos' 
    
    def __str__(self):
        return self.tipo_proyecto
    
    
    
            
 
   
        