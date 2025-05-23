from django.shortcuts import render
from .models import Postagem

def lista_postagens(request):
 postagens = Postagem.objects.all().order_by('-data_criacao')
 return render(request, 'blog/lista_postagens.html', {'postagens': postagens})
