from django.db import models

class Produto (models.Model):
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=100)
    unidade_medida = models.CharField(max_length=2)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fornecedor = models.CharField(max_length=14)

    