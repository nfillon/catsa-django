from django import forms
from clientes.models import Cliente, Proyecto




class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre_cliente']

class ProyectosForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['tipo_proyecto', 'nombre_proyecto' , 'year' , 'autor', 'clientes' ]