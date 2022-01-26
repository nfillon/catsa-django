from django.db import models

class Contacto(models.Model):
    Nombre=models.CharField(max_length=200)
    Apellido=models.CharField(max_length=200)
    Email=models.EmailField()
    Telefono=models.CharField(max_length = 15)
    Asunto=models.CharField(max_length=200)
    Mensaje=models.TextField()
    
    def __str__(self):
        return self.Nombre
        
    
    
      