from django .urls import path
from .views import (
    ProfessorListCreateAPIView,
    ProfessorRetrieveUpdateDestroyAPIView,
    DisciplinaListCreateAPIView,
    DisciplinaListCreateAPIView,
    ReservasProfessorList,
    DisciplinasProfessorList,
    ReservaDeClasseListCreateAPIView,
    ReservaDeClasseRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
   path('professor/', view=ProfessorListCreateAPIView.as_view(), name='Professor-GET-POST'),
   path('professor/<int:pk>', view=ProfessorRetrieveUpdateDestroyAPIView.as_view(), name='Professor-PUT-DELETE-GET'),

   path('disciplina/', view=DisciplinaListCreateAPIView.as_view(), name='Disciplina-GET-POST'),
   path('disciplina/<int:pk>/', view=DisciplinaListCreateAPIView.as_view(), name='Disciplina-PUT-DELETE-GET'),
   path('minhas-reservas/', view=ReservasProfessorList.as_view()), 
   path('minhas-disciplinas/', view=DisciplinasProfessorList.as_view()),

   path('disciplina/', view=ReservaDeClasseListCreateAPIView.as_view(), name='ReservaDeClasse-GET-POST'),
   path('disciplina/<int:pk>/', view=ReservaDeClasseRetrieveUpdateDestroyAPIView.as_view(), name='ReservaDeClasse-PUT-DELETE-GET'),
]