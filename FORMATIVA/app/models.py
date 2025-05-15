from django.db import models

class Professor(models.Model):
    NI = models.PositiveIntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)
    data_de_nascimento = models.DateField()
    data_de_contratacao = models.DateField()

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=50, primary_key=True)
    curso = models.CharField(max_length=100)
    carga_horaria = models.TimeField()
    descricao = models.CharField(max_length=300)
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Sala(models.Model):
    nome_sala = models.CharField(max_length=15)
    capacidade_de_pessoas = models.IntegerField()
    localidade = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)

    def __str__(self):
        return self.nome_sala

class ReservaDeClasse(models.Model):
    data_de_inicio = models.DateField()
    data_de_termino = models.DateField()

    TURNOS = (
        ('D', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
        ('N/A', 'Não Identificado'),
    )

    periodo = models.CharField(max_length=3, choices=TURNOS, default='N/A')
    sala_reservada = models.ForeignKey(Sala, on_delete=models.CASCADE)
    professor_responsavel = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina_associada = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.disciplina_associada} - {self.data_de_inicio} ({self.periodo})"
