from django.db import models
from treebeard.mp_tree import MP_Node


class Empresa(MP_Node):
    ativa = models.BooleanField('Ativa', default=True)
    nome = models.CharField(max_length=250)
    codigo = models.CharField(max_length=30)

    # criado automaticamente pela treebeard
    # mae = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.codigo, self.nome)
