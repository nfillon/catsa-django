from django import forms
from clientes.models import Cliente, Proyecto
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 

class ClienteForm(forms.ModelForm):
    
    nombre_cliente = forms.CharField(max_length=50, validators=[RegexValidator(regex='^[a-zA-Z]*$')])

    class Meta:
        model = Cliente
        fields = ['nombre_cliente']

        

class ProyectosForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['tipo_proyecto', 'nombre_proyecto' , 'year' , 'autor', 'clientes', 'imagen']
        
        
class  UserRegistrationForm(UserCreationForm):
    email = forms.EmailField() 
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput) 
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User 
        fields = ['username','email', 'password1', 'password2']
        help_text ={k: "" for k in fields}
         
     

    