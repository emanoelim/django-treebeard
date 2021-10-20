from rest_framework import serializers

from empresa.models import Empresa, EmpresaAL


class EmpresaSerializer(serializers.ModelSerializer):
    mae = serializers.SerializerMethodField()

    class Meta:
        model = Empresa
        fields = '__all__'

    @staticmethod
    def get_mae(instance):
        codigo = instance.codigo
        empresa = Empresa.objects.filter(codigo=codigo).first()
        mae = empresa.get_parent()
        if mae:
            return mae.nome
        return None


class EmpresaALSerializer(serializers.ModelSerializer):
    mae = serializers.SerializerMethodField()

    class Meta:
        model = EmpresaAL
        exclude = ('parent', )

    @staticmethod
    def get_mae(instance):
        mae = instance.parent
        if mae:
            return mae.nome
        return None
