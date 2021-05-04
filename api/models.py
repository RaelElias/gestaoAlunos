from django.db import models

class Aluno(models.Model):
    codigo_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    data_nascimento = models.DateField(u'Data de nascimento')
    cpf = models.CharField(u'CPF', max_length=100)
    telefone = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.codigo_aluno} - {self.nome}'

class Matricula(models.Model):
    codigo_matricula = models.AutoField(primary_key=True)
    codigo_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.CharField(max_length=254)
    status = models.BooleanField(default=True)

    def __str__(self):
        return  f'{self.codigo_matricula}'

class Suspender(models.Model):
    codigo_matricula = models.OneToOneField(Matricula, related_name='suspender', on_delete=models.CASCADE, primary_key=True)
    motivo = models.TextField()
    
    def __str__(self):
        return f'{self.codigo_matricula}'