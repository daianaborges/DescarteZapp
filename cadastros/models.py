from django.db import models

# Create your models here.

class Doadores(models.Model):
    nome = models.CharField(max_length=20, null=False, blank=False)
    sobrenome = models.CharField(max_length=20, null=False, blank=False)
    dataNascimento = models.DateField(max_length=10, null=False, blank=False, verbose_name="Data de Nascimento")
    endereco = models.CharField(max_length=100, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    complemento = models.CharField(max_length=10, null=False, blank=False)
    bairro = models.CharField(max_length=20, null=False, blank=False)
    cidade = models.CharField(max_length=20, null=False, blank=False)
    telefonefixo = models.CharField(max_length=20, null=False, blank=False, verbose_name="Telefone Fixo")
    celular = models.CharField(max_length=20, null=False, blank=False)



    def __str__(self):
        return "{} ({})".format(self.nome, self.bairro)

class Doacao(models.Model):
    d_celular = models.ForeignKey(Doadores, on_delete=models.CASCADE)
    quantidade = models.FloatField(verbose_name='Quantidade (l)')
    descricao = models.CharField(max_length=300, null=False, blank=False, verbose_name="Descrição")
       

    def __str__(self):
        return "{} ({})".format(self.d_celular, self.d_celular.quantidade)