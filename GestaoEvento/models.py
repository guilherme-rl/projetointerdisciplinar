"""
Definition of models.
"""

from tkinter import CASCADE
from django.db import models

# Create your models here.

class Entidade(models.Model):
    escolha_entidade = [
        ('U', 'Usuário'),
        ('C', 'Cliente'),
        ('P', 'Prestador'),]
    nome_razao = models.CharField(max_length=200)
    data_nascimento_criacao = models.DateField(null=True)
    cpf_cnpj = models.CharField(max_length=14)
    tipo = models.CharField(max_length=1, choices=escolha_entidade, default='C')
    excluido = models.BooleanField(default=False)
    login = models.CharField(max_length=200, default='')
    senha = models.CharField(max_length=200, default='')
    descricao_servico = models.CharField(max_length=200, default='')
    

class Endereco(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, related_name='endereco')
    cep = models.CharField(max_length=8, default='')
    bairro = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200, default='')
    estado = models.CharField(max_length=200, default='')
    excluido = models.BooleanField(default=False)
    principal = models.BooleanField(default=False)


class Email(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, related_name='email')
    email = models.CharField(max_length=200)


class Telefone(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, related_name='telefone')
    telefone = models.CharField(max_length=30)


class ItemLocacao(models.Model):
    descricao = models.CharField(max_length=200)
    excluido = models.BooleanField(default=False)


class UnidadeMedida(models.Model):
    descricao = models.CharField(max_length=200)
    sigla = models.CharField(max_length=3, default='')
    excluido = models.BooleanField(default=False)
    

class Ingrediente(models.Model):
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.CASCADE)
    custo_unidade = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=200)
    excluido = models.BooleanField(default=False)


class Prato(models.Model):
    descricao = models.CharField(max_length=200)
    rendimento = models.DecimalField(max_digits=10, decimal_places=4)
    excluido = models.BooleanField(default=False)
    ingredientes = models.ManyToManyField(
        Ingrediente,
        through="PratoIngredienteAux",
        through_fields=("prato", "ingrediente")
    )


class PratoIngredienteAux(models.Model):
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    quantidade = models.DecimalField(max_digits=10, decimal_places=4)


class Orcamento(models.Model):
    cliente = models.ForeignKey(Entidade, on_delete=models.CASCADE, related_name='orcamentos')
    quantidade_pessoas = models.IntegerField()
    data_evento = models.DateField(null=True)
    excluido = models.BooleanField(default=False)
    itens_locacao = models.ManyToManyField(
        ItemLocacao, 
        through="OrcamentoItemLocacaoAux",
        through_fields=("orcamento", "item_locacao")
    )
    pratos = models.ManyToManyField(
        Prato, 
        through="OrcamentoPratoAux",
        through_fields=("orcamento", "prato")
    )
    prestadores = models.ManyToManyField(
        Entidade, 
        through="OrcamentoPrestadorAux",
        through_fields=("orcamento", "prestador")
    )


class Contrato(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
    data_impressao = models.DateField(null=True)
    excluido = models.BooleanField(default=False)


class OrcamentoItemLocacaoAux(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
    item_locacao = models.ForeignKey(ItemLocacao, on_delete=models.CASCADE)
    quantidade = models.IntegerField()


class OrcamentoPratoAux(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)


class OrcamentoPrestadorAux(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
    prestador = models.ForeignKey(Entidade, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)