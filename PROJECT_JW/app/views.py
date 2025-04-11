from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .models import UserAbs
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    cargo= request.data.get('cargo')
    telefone = request.data.get('telefone')

    if not username or not password or not email or not cargo or not telefone:
        return Response({'ERRO' : 'Informações Insuficientes'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(username = username).exists():
        return Response({"ERRO" : 'Username já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(email = email).exists():
        return Response({'Erro':'Email Já existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    usuario = UserAbs.objects.create_user(
        username = username,
        password = password,
        email = email,
        cargo = cargo,
        telefone = telefone
    )
    return Response({'Criado' : f'Usuário {usuario} criado'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar(request):
    username = request.data.get('username')
    password = request.data.get('password')

    usuario = authenticate(username=username, password=password)

    if usuario:
        refresh = RefreshToken.for_user(usuario)
        return Response({
            'access' : str(refresh.access_token),
            'refresh' : str(refresh),
        }, status=status.HTTP_200_OK)

    else:
        return Response({'Erro' : 'Usuario ou senha inválido'}, status=status.HTTP_401_UNAUTHORIZED)
        

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_protegido(request):
    return Response({'Mensagem':'Ola DS14'}, status=status.HTTP_200_OK)