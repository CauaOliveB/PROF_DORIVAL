from .models import Tarefa 
from rest_framework import serializers

class TarefaSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Tarefa
        fields = '__all__'