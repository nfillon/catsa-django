from django.urls import path
from . import views


urlpatterns = [
   path('contactos', views.conctactoWeb, name="Contactos"),
]

