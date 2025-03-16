from django.urls import path
from . import views
urlpatterns = [
    path('produto/', views.produto, name="produto")
]
