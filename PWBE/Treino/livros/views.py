from django.shortcuts import render
from .models import Livro
from .serializers import LivroSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def listar_livros(request):
    return render(request, 'livros.html')

@api_view(['GET', 'POST'])
def catalogo(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LivroSerializer(data=request.data) 
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    

