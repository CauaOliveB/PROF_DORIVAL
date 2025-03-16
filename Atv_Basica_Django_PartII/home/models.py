from django.db import models


class produto(models.Model):
    nome = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='produtos/')
    preco = models.PositiveBigIntegerField()

    def __str__(self):
        return self.nome, self.imagem, self.preco