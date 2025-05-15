from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response 
from .serializers import ProfessorSerializer
from .models import Professor

@api_view(['GET'])
def listar_professores(request):
    professores = Professor.objects.all()
    serializer = ProfessorSerializer (professores, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def cadastrar_professores(request):
    if request.method == 'POST':
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def atualizer_cadastro_professores(request):