from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProfessorSerializer, DisciplinaSerializer, ReservaDeClasseSerializer
from .models import Professor, Disciplina, ReservaDeClasse
from rest_framework.permissions import IsAuthenticated
from .permissions import IsManager

 
"""""

*--------------------------------*
|                                |
|          Professores           |
|                                |
*--------------------------------*

"""""

class ProfessorListCreateAPIView(ListCreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsManager()]
    
class ProfessorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    
    def get_permissions(self):
        return[IsManager()]
    
"""""

*--------------------------------*
|                                |
|          Disciplina            |
|                                |
*--------------------------------*

"""""

class DisciplinaListCreateAPIView(ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsManager]

class DisciplinaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    
    def get_permissions(self):
        return[IsManager()]
    

"""""

*--------------------------------*
|                                |
|            Reserva             |
|                                |
*--------------------------------*

"""""

class ReservaDeClasseListCreateAPIView(ListCreateAPIView):
    queryset = ReservaDeClasse.objects.all()
    serializer_class = ReservaDeClasseSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsManager]

class ReservaDeClasseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ReservaDeClasse.objects.all()
    serializer_class = ReservaDeClasseSerializer
    
    def get_permissions(self):
        return[IsManager()]
    