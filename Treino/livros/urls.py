from django.urls import path 
from . import views

urlpatterns = [
    path('ListarExemplares/', views.listar_livros),
    path('api/livros/', views.catalogo),
]