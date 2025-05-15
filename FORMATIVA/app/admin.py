from django.contrib import admin
from .models import Professor, Disciplina, ReservaDeClasse, Sala

admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(ReservaDeClasse)
admin.site.register(Sala)