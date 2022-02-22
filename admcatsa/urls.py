from django.urls import path
from admcatsa import views
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('catsa/', views.list_client , name="list_client"),
    path('catsa/new', views.create_cliente , name="create_cliente"),
    path('catsa/newproyectos', views.create_proyecto , name="create_proyecto"),
    path('catsa/update/<int:id>/', views.update_cliente , name="update_cliente"),
    path('catsa/updateproyecto/<int:id>/', views.update_proyecto , name="update_proyecto"),  
    path('catsa/delete/<int:id>/', views.delete_cliente , name="delete_cliente"),
    path('catsa/deleteproyecto/<int:id>/', views.delete_proyecto , name="delete_proyecto"),
    path('mensajes/', views.list_mensajes , name="list_mensajes"),
    path('mensajes/delete/<int:id>/', views.delete_mensaje , name="delete_mensaje"),
    path('register/', views.register , name="register"),
    path('login/', LoginView.as_view(template_name="admcatsa/login.html") , name="login"),
    path('accounts/login/', LoginView.as_view(template_name="admcatsa/login.html") , name="login"),
    path('logout/', LogoutView.as_view(template_name="admcatsa/logout.html") , name="logout"),
    ]

