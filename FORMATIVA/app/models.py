from django.db import models

class Professor(models.Model):
    NI = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    data_de_nascimento = models.DateField()
    data_de_contratacao = models.DateField()

class Disciplina(models.Model):
    nome = models.CharField(max_lenght=50, primary_key=True)
    curso = models.CharField(max_lenght=100)
    carga_horaria = models.TimeField()
    descricao = models.CharField(max_lenght=300)
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.CASCADE)

class Sala(models.Model):
    nome_sala=models.CharField(max_length=15)
    capacidade_de_pessoas = models.IntegerField()
    localidade = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)


class Reserva_de_classe(models.Model):
    data_de_inicio = models.DateField()
    data_de_termino = models.DateField()
    choices = (
        ('Não Identificado' , 'N/A'),
        ('Manhã' , 'D'),
        ('Tarde' , 'T'),
        ('Noite' , 'N'), 
    )

    periodo = models.CharField(max_length=1,choices=choices,default='N')
    sala_reservada = models.ForeignKey(Sala, on_delete=models.CASCADE, on_update=models.CASCADE)
    professor_responsavel = models.ForeignKey(Professor, to_field='nome')
    disciplina_associada= models.ForeignKey(Disciplina, to_field='nome')
    


