from admcatsa import views
from django.urls import path



urlpatterns = [
    path('catsa/', views.list_client , name="list_client"),
    path('catsa/new', views.create_cliente , name="create_cliente"),
    path('catsa/update/<int:id>/', views.update_cliente , name="update_cliente"),
    path('catsa/updateproyecto/<int:id>/', views.update_proyecto , name="update_proyecto"),  
    path('catsa/delete/<int:id>/', views.delete_cliente , name="delete_cliente"),
    path('catsa/deleteproyecto/<int:id>/', views.delete_proyecto , name="delete_proyecto"),
    ]
