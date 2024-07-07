"""
Definition of models.
"""

from typing import Iterable
from django.db import models
from datetime import date
from django.db import transaction


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



class PorteCirurgico(models.Model):
    descricao = models.CharField(max_length=150)
    tempo_minutos = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = 'PorteCirurgicos'
        verbose_name = 'PorteCirurgico'

class PorteCirurgicoCirurgia(models.Model):
    descricao = models.ForeignKey(PorteCirurgico, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if self.produto:
            self.total = self.produto.preco * self.quantidade  # Calculate total based on quantity and unit cost
        super().save(*args, **kwargs)

    def __str__(self):
        return f"PorteCirurgicoCirurgia {self.descricao} - {self.produto}"
    
    class Meta:
        verbose_name_plural = 'PorteCirurgicoCirurgias'
        verbose_name = 'PorteCirurgicoCirurgia'


from django.db import transaction

class Cirurgia(models.Model):
    portecirurgico = models.ForeignKey(PorteCirurgico, on_delete=models.CASCADE, null=True)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    tempoCirurgia = models.IntegerField(default=0)
    tempoInternacao = models.IntegerField(default=0)
    localInternacao = models.CharField(max_length=100, default='HOSPITAL')
    custoFixo = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0.00)
    custoVariavel = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0.00)
    custoTotal = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    data = models.DateField(default=date.today)

    def save(self, *args, **kwargs):
        self.tempoCirurgia = self.portecirurgico.tempo_minutos if self.portecirurgico else None

        with transaction.atomic():
            # Salva a instância primeiro para garantir que ela tenha uma chave primária
            if not self.pk:
                super().save(*args, **kwargs)
            # Cria as linhas de cirurgia e calcula os custos
            self._create_linhas_cirurgia()
            self.calculate_costs()
            super().save(*args, **kwargs)

    def _create_linhas_cirurgia(self):
        if self.portecirurgico:
            porte_cirurgico_cirurgias = PorteCirurgicoCirurgia.objects.filter(descricao=self.portecirurgico)
            for pcc in porte_cirurgico_cirurgias:
                LinhasCirurgia.objects.get_or_create(
                    cirurgia=self,
                    codigo=pcc.produto,
                    defaults={
                        'quantidade': pcc.quantidade,
                        'custoUnitario': pcc.produto.preco,
                        'total': pcc.quantidade * pcc.produto.preco
                    }
                )

    def calculate_costs(self):
        self.custoFixo = sum(linha.total or 0 for linha in self.linhascirurgia_set.filter(codigo__tipoCusto='CUSTO FIXO'))
        self.custoVariavel = sum(linha.total or 0 for linha in self.linhascirurgia_set.filter(codigo__tipoCusto='CUSTO VARIAVEL'))
        self.custoTotal = (self.custoFixo or 0) + (self.custoVariavel or 0)

    def update_costs(self):
        self.calculate_costs()
        super().save(update_fields=['custoFixo', 'custoVariavel', 'custoTotal'])

    def __str__(self):
        return f"Cirurgia {self.procedimento} - {self.paciente}"
    
    class Meta:
        verbose_name_plural = 'Cirurgias'
        verbose_name = 'Cirurgia'


    
class LinhasCirurgia(models.Model):
    cirurgia = models.ForeignKey(Cirurgia, on_delete=models.CASCADE)
    codigo = models.ForeignKey(Produto, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=150, blank=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE, null=True, blank=True)
    custoUnitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.00)
    quantidade = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        self.total = self.quantidade * self.custoUnitario
        self.descricao = self.codigo.descricao if self.codigo else None
        self.unidade = self.codigo.unidade if self.codigo else None
        self.custoUnitario = self.codigo.preco if self.codigo else None
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Linha {self.codigo} - {self.descricao}"
    
    class Meta:
        verbose_name_plural = 'LinhasCirurgias'
        verbose_name = 'LinhaCirurgia'

