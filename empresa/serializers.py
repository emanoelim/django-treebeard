from rest_framework import serializers

from empresa.models import Empresa


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
