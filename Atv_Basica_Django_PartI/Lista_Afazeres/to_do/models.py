from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.TextField()
    conclusao_sim = 'Concluído'
    conclusao_nao = 'Não concluído'
    conclusao_choice = [
        (conclusao_sim, 'Concluído'),
        (conclusao_nao, 'Não concluído'),
    ]
    conclusao = models.CharField(
        max_length=13,
        choices = conclusao_choice,
        default = conclusao_nao,
    )

    def __str__(self):
        return self.titulo
