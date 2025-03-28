from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from .models import UserAbs
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
        return Response({'Aviso' : 'Usuário Autenticado com Sucesso'}, status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    telefone = request.data.get('telefone')
    endereco = request.get.data('endereço')
    idade = request.data.get('idade')
    escolaridade = request.data.get('escolaridade')
    animais = request.data.get('animais')
    biografia = request.data.get('biografia')

    if not username or not password or not email:
        return Response({'ERROR' : 'Insufficient Informations'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(username = username).exists():
        return Response({'ERROR' : 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(email = email).exists():
        return Response({'ERROR' : 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = UserAbs.objects.create_user(
        username = username,
        password = password,
        email = email,
        telefone = telefone,
        endereco = endereco,
        idade = idade,
        escolaridade = escolaridade,
        animais = animais,
        biografia = biografia
    ) 
    return Response ({'CREATED' : f'User {user} created with success'}, satus=status.HTTP_201_CREATED)


@api_view(['POST'])
def logar(request):
     username = request.data.get('username')
     password = request.data.get('password')

     user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'access' : str(refresh.access_token),
            'refresh' : str(refresh),
        }, status=status.HTTP_200_OK)
    else:
        return Response({'Erro' : 'Usuario ou senha inválido'}, status=status.HTTP_401_UNAUTHORIZED)
        
