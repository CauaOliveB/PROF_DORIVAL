from django.db import models

class professor(models.Model):
    NI = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    data_de_nascimento = models.DateField()