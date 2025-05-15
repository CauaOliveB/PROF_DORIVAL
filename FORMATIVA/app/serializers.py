from rest_framework import serializers
from .models import Professor, Disciplina, ReservaDeClasse

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class ReservaDeClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaDeClasse
        fields = '__all__'