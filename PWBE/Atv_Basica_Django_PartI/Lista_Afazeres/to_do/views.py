from django.shortcuts import render
from .models import Tarefa
from rest_framework import serializers
from .serializers import TarefaSerilizer
from rest_framework.response import Response 
from rest_framework.decorators import api_view 


@api_view(['GET'])
def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    serializers = TarefaSerilizer(tarefas, many=True)
    return Response(serializers.data)



   
