from django.db import models


class Tarefa(models.Model):
    STATUS_CHOICES = [
        (1, "A fazer"),
        (2, "Fazendo"),
        (3, "Concluido")
    ]

    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, null=False, blank=False)
