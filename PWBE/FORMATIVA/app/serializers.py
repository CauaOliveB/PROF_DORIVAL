from rest_framework import serializers
from .models import Professor, Disciplina, ReservaDeClasse

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
    def create(self, validation_data):
        Professor.objects.create_user(
            username = validation_data['username'],
            password = validation_data['password'],
            email = validation_data['email'],

        )

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class ReservaDeClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaDeClasse
        fields = '__all__'

"""

{
   "username": "caua",
   "password": "123,
   "data_de_nascimento": "2005-05-05",
   "email": "caua@bosch.senai",

}

"""