from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def produto(request):
    return render(request, 'pagina_inicial.html')