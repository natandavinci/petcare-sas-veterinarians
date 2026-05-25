from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('clientes/', views.clientes, name='clientes'),
    path('clientes/<int:pk>/', views.paciente, name='paciente'),
    path('clientes/<int:id_cliente>/triagem/', views.triagem, name='triagem'),
    path('consultas/<int:pk>/', views.consulta, name='consulta'),
]