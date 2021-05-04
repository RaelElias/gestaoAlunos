from rest_framework import serializers
from api.models import Aluno, Matricula, Suspender


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields='__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(read_only=True, initial=True)
    class Meta:
        model = Matricula
        fields='__all__'
        # read_only_fields = ['status'] //Campo somente leitura (Aparecer apenas em listagem)

class SuspenderSerializer(serializers.ModelSerializer):
    suspender = MatriculaSerializer(read_only=True, many=True)
    class Meta:
        model = Suspender
        fields='__all__'
        
        
        