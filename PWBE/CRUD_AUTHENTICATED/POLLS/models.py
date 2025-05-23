from django.db import models

class Users(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    telefone = models.CharField(max_length=14)
    endereco = models.CharField(max_length=32)
    qnt_animais = models.PositiveIntegerField()
    escolariadade_choices = (
        ('NES', 'Não-Escolarizado'),
        ('FUN', 'Fundamental'),
        ('ENM', 'Ensino Médio'),
        ('GRA', 'Graduação'),
        ('MES', 'Mestrado'),
        ('DOT', 'Doutorado'),
    )
    escolariadade = models.CharField(max_length=3, choices=escolariadade_choices, default='NES')

