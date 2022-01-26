from django.contrib import admin
from django.urls import path
from Catsaweb import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="Home"),
    path('insfrastructura', views.insfrastructura, name="Insfrastructuras"),
    # path('contacto/', views.conctacto, name="Contactos")
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)