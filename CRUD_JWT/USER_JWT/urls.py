from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('criarusuario/', view=views.create_user, name='create_user'),
]