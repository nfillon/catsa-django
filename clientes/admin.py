from django.contrib import admin
from .models import Cliente, Proyecto

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class ProyectoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Cliente, ClienteAdmin)

admin.site.register(Proyecto, ProyectoAdmin)