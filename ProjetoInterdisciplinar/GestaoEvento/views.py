from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from GestaoEvento.models import *

# Create your views here.

def index(request):
    return render(
        request,
        'GestaoEvento/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def Contato(request):
    return render(
        request,
        'GestaoEvento/Contato.html',
        {
            'title':'Contato',
            'year':datetime.now().year,
        }
    )


############## Cliente ##############
def IndexCliente(request):
    
    clientes = Cliente.objects.all()

    return render(
        request,
        'Cliente/Cliente.html',
        {
            'title':'Cliente',
            'clientes': clientes
        }
    )


def ModalNovoCliente(request):

    return render(
        request,
        'Cliente/ModalNovo.html',
    )


def NovoCliente(request):
    
    try:
        novo_cliente = Cliente(
            nome_razao=request.POST.get('nome'),
            data_nascimento_criacao=request.POST.get('data_nasc'),
            cpf_cnpj=request.POST.get('cpf_cnpj'),
        )
        
        novo_cliente.save()

        return JsonResponse({'success': True})
    
    except Exception as e:
        print(e)


############## Prestador ##############
def IndexPrestador(request):
    
    prestadores = Prestador.objects.all()

    return render(
        request,
        'Prestador/Prestador.html',
        {
            'title':'Prestadores',
            'prestadores': prestadores
        }
    )


def ModalNovoPrestador(request):

    return render(
        request,
        'Prestador/ModalNovo.html',
    )


def NovoPrestador(request):

    return JsonResponse({'success': True})


############## Usuario ##############
def IndexUsuario(request):
    
    usuarios = Usuario.objects.all()

    return render(
        request,
        'Usuario/Usuario.html',
        {
            'title':'Prestadores',
            'usuarios': usuarios
        }
    )


def ModalNovoUsuario(request):

    return render(
        request,
        'Usuario/ModalNovo.html',
    )


def NovoUsuario(request):

    return JsonResponse({'success': True})


############## ItemLocacao ##############
def IndexItemLocacao(request):
    
    itens_locacao = ItemLocacao.objects.all()

    return render(
        request,
        'ItemLocacao/ItemLocacao.html',
        {
            'title':'Itens de Locação',
            'itenslocacao': itens_locacao
        }
    )


def ModalNovoItemLocacao(request):

    return render(
        request,
        'ItemLocacao/ModalNovo.html',
    )


def NovoItemLocacao(request):

    return JsonResponse({'success': True})


############## UnidadeMedida ##############
def IndexUnidadeMedida(request):
    
    unidades_medida = UnidadeMedida.objects.all()

    return render(
        request,
        'UnidadeMedida/UnidadeMedida.html',
        {
            'title':'Unidades de Medida',
            'unidadesmedida': unidades_medida
        }
    )


def ModalNovoUnidadeMedida(request):

    return render(
        request,
        'UnidadeMedida/ModalNovo.html',
    )


def NovoUnidadeMedida(request):

    return JsonResponse({'success': True})


############## Ingrediente ##############
def IndexIngrediente(request):
    
    ingredientes = Ingrediente.objects.all()

    return render(
        request,
        'Ingrediente/Ingrediente.html',
        {
            'title':'Ingredientes',
            'ingredientes': ingredientes
        }
    )


def ModalNovoIngrediente(request):

    return render(
        request,
        'Ingrediente/ModalNovo.html',
    )


def NovoIngrediente(request):

    return JsonResponse({'success': True})


############## Prato ##############
def IndexPrato(request):
    
    pratos = Prato.objects.all()

    return render(
        request,
        'Prato/Prato.html',
        {
            'title':'Pratos',
            'pratos': pratos
        }
    )


def ModalNovoPrato(request):

    return render(
        request,
        'Prato/ModalNovo.html',
    )


def NovoPrato(request):

    return JsonResponse({'success': True})


############## Orcamento ##############
def IndexOrcamento(request):
    
    orcamentos = Orcamento.objects.all()

    return render(
        request,
        'Orcamento/Orcamento.html',
        {
            'title':'Orçamentos',
            'orcamentos': orcamentos
        }
    )


def ModalNovoOrcamento(request):

    return render(
        request,
        'Orcamento/ModalNovo.html',
    )


def NovoOrcamento(request):

    return JsonResponse({'success': True})


############## Relatorio ##############
def IndexRelatorio(request):
    
    relatorios = ''

    return render(
        request,
        'Relatorio/Relatorio.html',
        {
            'title':'Relatórios',
            'relatorios': relatorios
        }
    )


def ModalNovoRelatorio(request):

    return render(
        request,
        'Relatorio/ModalNovo.html',
    )


def NovoRelatorio(request):

    return JsonResponse({'success': True})


############## Contrato ##############
def IndexContrato(request):
    
    contrato = ''

    return render(
        request,
        'Contrato/Contrato.html',
        {
            'title':'Contratos',
            'contrato': contrato
        }
    )


def ModalNovoContrato(request):

    return render(
        request,
        'Contrato/ModalNovo.html',
    )


def NovoContrato(request):

    return JsonResponse({'success': True})