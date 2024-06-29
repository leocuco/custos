"""
Definition of models.
"""

from django.db import models
from datetime import date


TIPO_CUSTO_CHOICES = (
    ('CUSTO FIXO', 'Custo Fixo'),
    ('CUSTO VARIAVEL', 'Custo Variavel'),
)
# Create your models here.

class Familia(models.Model):
    familia = models.CharField(max_length=10)
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Familias'
        verbose_name_plural = 'Familia'
    
class Produto(models.Model):
    codigo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    unidade = models.ForeignKey('Unidade', on_delete=models.CASCADE)
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, null=True)
    tipoCusto = models.TextField(choices=TIPO_CUSTO_CHOICES, null=True)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = 'Produtos'
        verbose_name = 'Produto'

class Procedimento(models.Model):
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = 'Procedimentos'
        verbose_name = 'Procedimento'

class Unidade(models.Model):
    sigla = models.CharField(max_length=10)
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.sigla
    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'


class Especialidade(models.Model):
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = 'Especialidade'
        verbose_name = 'Especialidade'

class Paciente(models.Model):
    apelido= models.CharField(max_length=25)
    nome = models.CharField(max_length=150)
    datanacimento = models.DateField()
    localnascimento = models.CharField(max_length=20)
    nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome + self.apelido
    
    class Meta:
        verbose_name_plural = 'Pacientes'
        verbose_name = 'Paciente'



class Cirurgia(models.Model):
    procedimento = models.ForeignKey(Procedimento, on_delete= models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    tempoCirurgia = models.IntegerField()
    tempoInternacao = models.IntegerField()
    localInternacao = models.CharField(max_length= 100)
    custoFixo = models.DecimalField(max_digits=10,decimal_places=2, null=True)
    custoVariavel = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    custoTotal = models.DecimalField(max_digits=10, decimal_places= 2)
    data = models.DateField(default=date.today)  # Campo data adicionado

    def __str__(self):
        return f"Cirurgia {self.procedimento} - {self.paciente}"
    
    class Meta:
        verbose_name_plural = 'Cirurgias'
        verbose_name = 'Cirurgia'
    

class LinhasCirurgia(models.Model):
    cirurgia = models.ForeignKey(Cirurgia, on_delete=models.CASCADE)
    codigo = models.ForeignKey(Produto, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=150, blank=True)  # Make it optional initially
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, null=True, blank=True)  # Allow blank initially
    custoUnitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Allow blank initially
    quantidade = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.descricao:
            self.descricao = self.codigo.descricao
        if not self.unidade:
            self.unidade = self.codigo.unidade
        if not self.custoUnitario:
            self.custoUnitario = self.codigo.preco  # Assuming 'preco' is the unit cost in 'Produto'
        self.total = self.quantidade * self.custoUnitario  # Calculate total based on quantity and unit cost
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Linha {self.codigo} - {self.descricao}"
    
    class Meta:
        verbose_name_plural = 'LinhasCirurgias'
        verbose_name = 'LinhaCirurgia'

