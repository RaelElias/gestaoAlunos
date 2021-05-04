from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response


from api.serializers import AlunoSerializer, MatriculaSerializer , SuspenderSerializer
from api.models import Aluno, Matricula , Suspender

class AlunoViewSet(viewsets.ModelViewSet):
    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()

class MatriculaViewSet(viewsets.ModelViewSet):
    serializer_class = MatriculaSerializer
    queryset = Matricula.objects.all()

class SuspenderViewSet(viewsets.ModelViewSet):
    serializer_class = SuspenderSerializer
    queryset = Suspender.objects.all()

    def create(self, request):
        # Modifica o status da matricula
        matricula_queryset = Matricula.objects.get(codigo_matricula=request.data['codigo_matricula'])
        matricula_queryset.status = False
        matricula_queryset.save()
        # Pega o request e preenche obj no formato serializer (json)
        serializer = SuspenderSerializer(data=request.data)
        # Validacao dos dados
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Mensagem erro
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
    def destroy(self, request, pk=None):
        instance = self.get_object()
        # Altera status da matricula
        matricula_queryset = Matricula.objects.get(codigo_matricula=instance.codigo_matricula.codigo_matricula)
        matricula_queryset.status = True
        matricula_queryset.save()
        # Deleta obj Matricula Suspensa
        instance.delete()
        return Response(request.data, status=status.HTTP_200_OK)