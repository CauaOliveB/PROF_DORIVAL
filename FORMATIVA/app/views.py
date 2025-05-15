from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProfessorSerializer, DisciplinaSerializer, ReservaDeClasseSerializer
from .models import Professor, Disciplina, ReservaDeClasse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
from .permissions import IsManager
from rest_framework import status
 

class DisciplinaListCreateAPIView(ListAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsManager]

@api_view(['GET'])
def ListarProfessoresView(request):
    queryset = Professor.objects.all()
    serializer = ProfessorSerializer (queryset, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def CadastrarProfessoresView(request):
    if request.method == 'POST':
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def atualizer_cadastro_professores(request):