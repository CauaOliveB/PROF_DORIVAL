from django .urls import path
from . import views 

urlpatterns = [
   path('professor/', view=views.ProfessorListCreateAPIView.as_view(), name='Professor-GET-POST'),
   path('professor/<int:pk>', view=views.ProfessorRetrieveUpdateDestroyAPIView.as_view(), name='Professor-PUT-DELETE-GET'),

   path('disciplina/', view=views.DisciplinaListCreateAPIView.as_view(), name='Disciplina-GET-POST'),
   path('disciplina/<int:pk>/', view=views.DisciplinaRetrieveUpdateDestroyAPIView.as_view(), name='Disciplina-PUT-DELETE-GET'),

   path('disciplina/', view=views.ReservaDeClasseListCreateAPIView.as_view(), name='ReservaDeClasse-GET-POST'),
   path('disciplina/<int:pk>/', view=views.ReservaDeClasseRetrieveUpdateDestroyAPIView.as_view(), name='ReservaDeClasse-PUT-DELETE-GET'),
]