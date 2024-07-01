from django.db import models


class Servicos(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    localizacao = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
    def __str__(self):
        return self.descricao
    def __str__(self):
        return self.localizacao