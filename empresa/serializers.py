from rest_framework import serializers

from empresa.models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):
    pai = serializers.SerializerMethodField()

    class Meta:
        model = Empresa
        fields = '__all__'

    @staticmethod
    def get_pai(instance):
        codigo = instance.codigo
        empresa = Empresa.objects.filter(codigo=codigo).first()
        pai = empresa.get_parent()
        if pai:
            return pai.nome
        return None
