from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class UserAbs(AbstractUser):
    biografia = models.CharField(max_length=250)
    idade = models.PositiveIntegerField(default=0)
    telefone = models.PositiveIntegerField(default=0)
    endereco = models.CharField(max_length=150)
    animais = models.IntegerField(default=0)

    escolha = (
        ('nal', 'NÃO ALFABEITZADO'),
        ('al', 'ALFABEITZADO'),
        ('ef', 'Ensino Fundamental'),
        ('em', 'Ensino Médio'),
        ('s', 'Superior'),
        ('m', 'Mestrado'),
        ('d', 'Doutorado'),
    )

    escolaridade = models.CharField(
        max_length=3,
        choices=escolha,  
        default="nal",  
)

def __str__(self):
    return self.username