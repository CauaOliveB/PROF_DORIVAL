from django.contrib import admin
from .models import Professor, Disciplina, ReservaDeClasse

admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(ReservaDeClasse)