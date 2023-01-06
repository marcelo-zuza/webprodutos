from django.db import models


class Participantes(models.Model):
    nome_completo = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    filme_favorito = models.CharField(
        max_length=60,
        blank=False,
        null=False
    )

    idade = models.IntegerField(
        default=0,
    )

    cidade = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    estado = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.nome_completo
