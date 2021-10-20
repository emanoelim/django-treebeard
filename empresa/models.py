from django.db import models
from treebeard.mp_tree import MP_Node
from treebeard.al_tree import AL_Node


class Empresa(MP_Node):
    ativa = models.BooleanField('Ativa', default=True)
    nome = models.CharField(max_length=250)
    codigo = models.CharField(max_length=30)

    # criado automaticamente pela treebeard
    # mae = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '%s - %s' % (self.codigo, self.nome)


class EmpresaAL(AL_Node):
    ativa = models.BooleanField('Ativa', default=True)
    nome = models.CharField(max_length=250)
    codigo = models.CharField(max_length=30)
    parent = models.ForeignKey('self',
                               related_name='children_set',
                               null=True,
                               blank=True,
                               db_index=True,
                               on_delete=models.DO_NOTHING)
    node_order_by = ['ativa', 'nome', 'codigo']

    def __str__(self):
        return '%s - %s' % (self.codigo, self.nome)
