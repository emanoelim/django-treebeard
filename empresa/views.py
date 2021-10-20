from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from empresa.models import Empresa, EmpresaAL
from empresa.serializers import EmpresaSerializer, EmpresaALSerializer


class EmpresaView(ModelViewSet):
    # queryset = Empresa.objects.all()
    queryset = EmpresaAL.objects.all()
    # serializer_class = EmpresaSerializer
    serializer_class = EmpresaALSerializer
    allowed_methdos = ['get']

    def create(self, request, *args, **kwargs):
        codigo_mae = request.data.get('mae')
        nome = request.data.get('nome')
        codigo = request.data.get('codigo')
        ativa = request.data.get('ativa')
        # empresa_mae = Empresa.objects.filter(codigo=codigo_mae).first()
        empresa_mae = EmpresaAL.objects.filter(codigo=codigo_mae).first()
        empresa_filha = empresa_mae.add_child(nome=nome, codigo=codigo, ativa=ativa)
        # serializer = EmpresaSerializer(empresa_filha)
        serializer = EmpresaALSerializer(empresa_filha)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # empresa = Empresa.objects.filter(codigo=instance.codigo).first()
        empresa = EmpresaAL.objects.filter(codigo=instance.codigo).first()
        empresa.delete()
        return Response(
            status=status.HTTP_200_OK
        )

    @action(methods=["get"], detail=True, url_path='mae')
    def empresa_mae(self, request, pk=None):
        # empresa = Empresa.objects.filter(id=pk).first()
        empresa = EmpresaAL.objects.filter(id=pk).first()
        empresa_mae = empresa.get_parent()
        # serializer = EmpresaSerializer(empresa_mae)
        serializer = EmpresaALSerializer(empresa_mae)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    @action(methods=["get"], detail=True, url_path='filhas')
    def empresas_filhas(self, request, pk=None):
        # empresa = Empresa.objects.filter(id=pk).first()
        empresa = EmpresaAL.objects.filter(id=pk).first()
        filhas = empresa.get_children()
        # serializer = EmpresaSerializer(filhas, many=True)
        serializer = EmpresaALSerializer(filhas, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    @action(methods=["get"], detail=True, url_path='descendentes')
    def empresas_decendentes(self, request, pk=None):
        # empresa = Empresa.objects.filter(id=pk).first()
        empresa = EmpresaAL.objects.filter(id=pk).first()
        descendentes = empresa.get_descendants()
        # serializer = EmpresaSerializer(descendentes, many=True)
        serializer = EmpresaALSerializer(descendentes, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    @action(methods=["get"], detail=True, url_path='ancestrais')
    def empresas_ancestrais(self, request, pk=None):
        # empresa = Empresa.objects.filter(id=pk).first()
        empresa = EmpresaAL.objects.filter(id=pk).first()
        ancestrais = empresa.get_ancestors()
        # serializer = EmpresaSerializer(ancestrais, many=True)
        serializer = EmpresaALSerializer(ancestrais, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    @action(methods=["get"], detail=True, url_path='irmas')
    def empresas_irmas(self, request, pk=None):
        # empresa = Empresa.objects.filter(id=pk).first()
        empresa = EmpresaAL.objects.filter(id=pk).first()
        irmas = empresa.get_siblings()
        # serializer = EmpresaSerializer(irmas, many=True)
        serializer = EmpresaALSerializer(irmas, many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
