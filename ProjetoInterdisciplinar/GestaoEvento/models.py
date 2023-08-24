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

    class Meta:
        abstract = True


class Usuario(Entidade):
    login = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.tipo = 'U'
        super().save(**args, **kwargs)


class Prestador(Entidade):
    descricao_servico = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.tipo = 'P'
        super().save(**args, **kwargs)


class Cliente(Entidade):
    def save(self, *args, **kwargs):
        self.tipo = 'C'
        super().save(**args, **kwargs)


class Estado(models.Model):
    descricao = models.CharField(max_length=200)


class Cidade(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=200)
    

class Endereco(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='endereco')
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE, related_name='endereco')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='endereco')
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    bairro = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200)


class Email(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='email')
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE, related_name='email')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='email')
    email = models.CharField(max_length=200)


class Telefone(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='telefone')
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE, related_name='telefone')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='telefone')
    telefone = models.CharField(max_length=30)


class ItemLocacao(models.Model):
    descricao = models.CharField(max_length=200)
    excluido = models.BooleanField(default=False)


class UnidadeMedida(models.Model):
    descricao = models.CharField(max_length=200)
    

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
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='orcamentos')
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
        Prestador, 
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
    prestador = models.ForeignKey(Prestador, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)