from datetime import datetime
from django.db import transaction, connection
from django.db.models import F, Q, Sum
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from GestaoEvento.models import *
import json
import re

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


# region Cliente 
def IndexCliente(request):

    return render(
        request,
        'Cliente/Cliente.html',
        {
            'title':'Cliente',
        }
    )
    
    
def TabelaClientes(request):
    
    busca = request.POST.get('busca')
    
    clientes = Entidade.objects.filter(Q(tipo='C') & Q(excluido=False))
    
    if busca:
        clientes = clientes.filter(nome_razao__icontains=busca)
    
    return render(
        request,
        'Cliente/Tabela.html',
        {
            'clientes': clientes,
            'busca': busca,
        }
    )


def ModalCliente(request):
    
    id = request.GET.get('id')
    cliente = Entidade()
    data_formatada = ''
    endereco_principal = Endereco()
    
    if id:
        cliente = Entidade.objects.get(id=id)
        data_formatada = cliente.data_nascimento_criacao.strftime('%Y-%m-%d')
        endereco_principal = cliente.endereco.get(principal=True)

    return render(
        request,
        'Cliente/ModalCliente.html',
        {
            'cliente': cliente,
            'data_formatada': data_formatada,
            'endereco_principal': endereco_principal,
        }
    )


def ModalDetalhesCliente(request):
    
    cliente_id = request.GET.get('id')
    cliente = Entidade.objects.get(pk=cliente_id)
    data_formatada = cliente.data_nascimento_criacao.strftime('%d/%m/%Y')
    endereco_principal = cliente.endereco.get(principal=True)
    cep_formatado = f'{endereco_principal.cep[:5]}-{endereco_principal.cep[5:]}'
    cpf_cnpj_formatado = ''
    if (len(cliente.cpf_cnpj) == 11):
        cpf_cnpj_formatado = f'{cliente.cpf_cnpj[:3]}.{cliente.cpf_cnpj[3:6]}.{cliente.cpf_cnpj[6:9]}-{cliente.cpf_cnpj[9:]}'
    else:
        cpf_cnpj_formatado = f'{cliente.cpf_cnpj[:2]}.{cliente.cpf_cnpj[2:5:1]}.{cliente.cpf_cnpj[5:8]}/{cliente.cpf_cnpj[8:12]}-{cliente.cpf_cnpj[12:]}'

    return render(
        request,
        'Cliente/ModalDetalhesCliente.html',
        {
            'cliente': cliente,
            'data_formatada': data_formatada,
            'endereco_principal': endereco_principal,
            'cpf_cnpj_formatado': cpf_cnpj_formatado,
            'cep_formatado': cep_formatado,
        }
    )


def ModalExcluirCliente(request):
    
    cliente_id = request.GET.get('id')
    cliente = Entidade.objects.get(pk=cliente_id)

    return render(
        request,
        'Cliente/ModalExcluirCliente.html',
        {
            'cliente': cliente
        }
    )


def SalvarCliente(request):
    try:
        with transaction.atomic():
            
            id = request.POST.get('id')
            data = datetime.strptime(request.POST.get('data_nasc'), '%Y-%m-%d')
            cliente = None
            
            if id != 'None':
                cliente = Entidade.objects.get(id=id)
                cliente.nome_razao = request.POST.get('nome')
                cliente.data_nascimento_criacao = data
                
                endereco = cliente.endereco.get(principal=True)
                endereco.cep = request.POST.get('cep').replace('-', '') if request.POST.get('cep') else ''
                endereco.bairro = request.POST.get('bairro')
                endereco.complemento = request.POST.get('endereco')
                endereco.cidade = request.POST.get('cidade')
                endereco.estado = request.POST.get('estado').upper()
                
                endereco.save()
                
            else:
                cpf = request.POST.get('cpf_cnpj')
                cpf = re.sub(r'[^0-9]', '', cpf)
                cliente = Entidade(
                    nome_razao = request.POST.get('nome'),
                    cpf_cnpj = cpf,
                    data_nascimento_criacao = data,
                    tipo = 'C',
                )
                cliente.save()
                
                cliente.endereco.create(
                    cep = request.POST.get('cep').replace('-', '') if request.POST.get('cep') else '',
                    bairro = request.POST.get('bairro'),
                    complemento = request.POST.get('endereco'),
                    cidade = request.POST.get('cidade'),
                    estado = request.POST.get('estado').upper(),
                    principal = True,
                )
            
            cliente.save()

            return JsonResponse({'sucesso': True})
    
    except Exception as e:
        print(e)
        
        return JsonResponse({'sucesso': False})
        

def ExcluirCliente(request):
    
    try:
        with transaction.atomic():
            
            cliente_id = request.POST.get('id')
            cliente = Entidade.objects.get(pk=cliente_id)
            
            cliente.excluido = True
            
            cliente.save()
            
            return JsonResponse({'sucesso': True})
    
    except Exception as e:
        print(e)
        return JsonResponse({'sucesso': False, 'erro': str(e) })

# endregion

# region Prestador
def IndexPrestador(request):
    

    return render(
        request,
        'Prestador/Prestador.html',
        {
            'title':'Prestador',
        }
    )


def SalvarPrestador(request):
    try:
        with transaction.atomic():
            
            id = request.POST.get('id')
            data = datetime.strptime(request.POST.get('data_nasc'), '%Y-%m-%d')
            prestador = None
            
            if id != 'None':
                prestador = Entidade.objects.get(id=id)
                prestador.nome_razao = request.POST.get('nome')
                prestador.data_nascimento_criacao = data
                
                endereco = prestador.endereco.get(principal=True)
                endereco.cep = request.POST.get('cep').replace('-', '') if request.POST.get('cep') else ''
                endereco.bairro = request.POST.get('bairro')
                endereco.complemento = request.POST.get('endereco')
                endereco.cidade = request.POST.get('cidade')
                endereco.estado = request.POST.get('estado').upper()
                
                endereco.save()
                
            else:
                cpf = request.POST.get('cpf_cnpj')
                cpf = re.sub(r'[^0-9]', '', cpf)
                prestador = Entidade(
                    nome_razao = request.POST.get('nome'),
                    cpf_cnpj = cpf,
                    data_nascimento_criacao = data,
                    tipo = 'P',
                )
                prestador.save()
                
                prestador.endereco.create(
                    cep = request.POST.get('cep').replace('-', '') if request.POST.get('cep') else '',
                    bairro = request.POST.get('bairro'),
                    complemento = request.POST.get('endereco'),
                    cidade = request.POST.get('cidade'),
                    estado = request.POST.get('estado').upper(),
                    principal = True,
                )
            
            prestador.save()

            return JsonResponse({'sucesso': True})
    
    except Exception as e:
        print(e)
        
        return JsonResponse({'sucesso': False})
        

    
def TabelaPrestadores(request):
    
    busca = request.POST.get('busca')

    prestadores= Entidade.objects.filter ((Q(tipo='P')) & Q(excluido=False))
    
    return render(
        request,
        'Prestador/Tabela.html',
        {
            'Prestadoes': prestadores,
             'busca': busca,
        }
    )


def ModalNovoPrestador(request):

    id = request.GET.get('id')
    prestador = Entidade()
    data_formatada = ''
    endereco_principal = Endereco()
    
    if id:
        prestador = Entidade.objects.get(id=id)
        data_formatada = prestador.data_nascimento_criacao.strftime('%Y-%m-%d')
        endereco_principal = prestador.endereco.get(principal=True)
    return render(
        request,
        'Prestador/ModalNovo.html',
        {
            'prestador': prestador,
            'data_formatada': data_formatada,
            'endereco_principal': endereco_principal,
        }
    )

def ModalDetalhesPrestador(request):
    
    prestador_id = request.GET.get('id')
    prestador = Entidade.objects.get(pk=prestador_id)
    data_formatada = prestador.data_nascimento_criacao.strftime('%d/%m/%Y')
    endereco_principal = prestador.endereco.get(principal=True)
    cep_formatado = f'{endereco_principal.cep[:5]}-{endereco_principal.cep[5:]}'
    cpf_cnpj_formatado = ''
    if (len(prestador.cpf_cnpj) == 11):
        cpf_cnpj_formatado = f'{prestador.cpf_cnpj[:3]}.{prestador.cpf_cnpj[3:6]}.{prestador.cpf_cnpj[6:9]}-{prestador.cpf_cnpj[9:]}'
    else:
        cpf_cnpj_formatado = f'{prestador.cpf_cnpj[:2]}.{prestador.cpf_cnpj[2:5:1]}.{prestador.cpf_cnpj[5:8]}/{prestador.cpf_cnpj[8:12]}-{prestador.cpf_cnpj[12:]}'

    return render(
        request,
        'Prestador/ModalDetalhesPrestador.html',
        {
            'prestador': prestador,
            'data_formatada': data_formatada,
            'endereco_principal': endereco_principal,
            'cpf_cnpj_formatado': cpf_cnpj_formatado,
            'cep_formatado': cep_formatado,
        }
    )

def ModalExcluirPrestador(request):
    
    prestador_id = request.GET.get('id')
    prestador = Entidade.objects.get(pk=prestador_id)
    
    return render(
        request,
        'Prestador/ModalExcluir.html',
        {
            'Prestador' : prestador 
        }
    )
def ExcluirPrestador(request):
    
    try:
        with transaction.atomic():
            
            prestador_id = request.POST.get('id')
            prestador = Entidade.objects.get(pk=prestador_id)
            
            prestador.excluido = True
            
            prestador.save()
            
            return JsonResponse({'sucesso': True})
    
    except Exception as e:
        print(e)
        return JsonResponse({'sucesso': False, 'erro': str(e) })

# endregion

# region Usuario
def IndexUsuario(request):
    
    usuarios = Entidade.objects.filter(tipo='U')

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

# endregion

# region ItemLocacao
def IndexItemLocacao(request):
     
    itemlocacao = ItemLocacao.objects.all()

    return render(
        request,
        'ItemLocacao/ItemLocacao.html',
        {
            'title':'Itens Locação',
            'itenslocacao': itemlocacao
        }
    )


def TabelaItensLocacao(request):

    busca = request.POST.get('busca')     

    itemlocacao = ItemLocacao.objects.filter(excluido=False)
    
    if busca:
        itemlocacao = itemlocacao.filter(Q(descricao__icontains=busca) | Q(id__icontains=busca))
    

    return render(
        request,
        'ItemLocacao/Tabela.html',
        {
            'itens_locacao': itemlocacao,
            'busca': busca,
        }
    )

def ModalNovoItemLocacao(request):
    
    id =request.GET.get('id')
    
    itemlocacao = ItemLocacao()

    if id:
        itemlocacao = ItemLocacao.objects.get(pk=id)
        

    return render(
        request,
        'ItemLocacao/ModalNovo.html',
        {
            'itemlocacao' : itemlocacao,
        }
    
    )

def ModalExcluirItemLocacao(request):

    id = request.GET.get('id')
    itemlocacao = ItemLocacao.objects.get(pk=id)
    
    return render(
        request,
        'ItemLocacao/ModalExcluir.html',
        {
            'itemlocacao': itemlocacao
        }
    )


def SalvarItemLocacao(request):   

    try:
        with transaction.atomic(): 

            id = request.POST.get('id')

            itemlocacao = ItemLocacao()

            if id:     
                itemlocacao = ItemLocacao.objects.get(id=id)

            itemlocacao.descricao = request.POST.get('descricao')
            itemlocacao.custo_unitario = request.POST.get('custo_unitario')
        

            itemlocacao.save()
    
        return JsonResponse({'sucesso': True})
        
    except Exception as e :
        print(e)

        return JsonResponse({'sucesso': False })

def ExcluirItemLocacao(request):

    try:
        with transaction.atomic():
            
            id = request.POST.get('id')
            itemlocacao= ItemLocacao.objects.get(pk=id)
           
            itemlocacao.excluido = True

            itemlocacao.save()
            
            return JsonResponse ({'sucesso' : True})

    except Exception as e :
        print (e)
        return JsonResponse({'sucesso' : False, 'erro' : str(e)})
    
# endregion

# region UnidadeMedida
def IndexUnidadeMedida(request):
    
    # unidades_medida = UnidadeMedida.objects.all()

    return render(
        request,
        'UnidadeMedida/UnidadeMedida.html',
        {
            'title':'Unidades de Medida',
            # 'unidadesmedida': unidades_medida
        }
    )


def TabelaUnidadeMedida(request):
    
    busca = request.POST.get('busca')
    
    unidade_medida = UnidadeMedida.objects.filter(excluido=False)
    
    if busca:
        unidade_medida = unidade_medida.filter(Q(descricao__icontains=busca) | Q(sigla__icontains=busca))
    
    return render(
        request,
        'UnidadeMedida/Tabela.html',
        {
            'unidades_medida': unidade_medida,
            'busca': busca,
        }
    )



def ModalUnidadeMedida(request):
    
    id = request.GET.get('id')
    
    unidadeMedida = UnidadeMedida()
    
    if id:
        unidadeMedida = UnidadeMedida.objects.get(pk=id)

    return render(
        request,
        'UnidadeMedida/ModalUnidadeMedida.html',
        {
            'unidade_medida': unidadeMedida,
        }
    )
def ModalExcluirUnidadeMedida(request):
    
    id = request.GET.get('id')
    unidadeMedida = UnidadeMedida.objects.get(pk=id)

    return render(
        request,
        'UnidadeMedida/ModalExcluirUnidadeMedida.html',
        {
            'unidade_medida': unidadeMedida
        }
    )


def SalvarUnidadeMedida(request):
    
    try:
        with transaction.atomic():
        
            id = request.POST.get('id')
            
            unidadeMedida = UnidadeMedida()
            
            if id != 'None':
                unidadeMedida = UnidadeMedida.objects.get(id=id)
                
            unidadeMedida.sigla = request.POST.get('sigla')
            unidadeMedida.descricao = request.POST.get('descricao')
                
            unidadeMedida.save()

            return JsonResponse({'sucesso': True})
    
    except Exception as e:
        print(e)
        
        return JsonResponse({'sucesso': False})
    
def ExcluirUnidadeMedida(request):
    
    try:
        with transaction.atomic():
            
            id = request.POST.get('id')
            unidadeMedida = UnidadeMedida.objects.get(pk=id)
            
            unidadeMedida.excluido = True
            
            unidadeMedida.save()
            
            return JsonResponse({'sucesso': True})
    
    except Exception as e:
        print(e)
        return JsonResponse({'sucesso': False, 'erro': str(e) })

# endregion

# region Ingrediente
def IndexIngrediente(request):
    
    # ingredientes = Ingrediente.objects.all()

    return render(
        request,
        'Ingrediente/Ingrediente.html',
        {
            'title':'Ingredientes',
            # 'ingredientes': ingredientes
        }
    )
    
    
def TabelaIngrediente(request):
    
    busca = request.POST.get('busca')
    
    ingredientes = Ingrediente.objects.filter(excluido=False)
    
    if busca:
        ingrediente = ingrediente.filter(Q(descricao__icontains=busca) | Q(unidade_medida__descricao=busca))
    
    return render(
        request,
        'Ingrediente/Tabela.html',
        {
            'ingredientes': ingredientes,
            'busca': busca,
        }
    )


def ModalIngrediente(request):
    
    unidadesMedida = list(UnidadeMedida.objects.filter(excluido=False))
    
    id = request.GET.get('id')
    
    ingrediente = Ingrediente()
    ingrediente.custo_unitario = ''
    
    if id:
        ingrediente = Ingrediente.get(pk=id)
    
    dados = {}
    
    for item in unidadesMedida:
        dados[item.id] = item.sigla

    return render(
        request,
        'Ingrediente/ModalIngrediente.html',
        {
            'unidades_medida': dados,
            'ingrediente': ingrediente,
        },
    )


def SalvarIngrediente(request):

    try:
        with transaction.atomic():
        
            id = request.POST.get('id')
            
            ingrediente = Ingrediente()
            
            if id != 'None':
                ingrediente = Ingrediente.objects.get(pk=id)
                
            ingrediente.descricao = request.POST.get('descricao')
            ingrediente.unidade_medida_id = request.POST.get('unidade-medida')
            ingrediente.custo_unitario = request.POST.get('custo-unidade')
                
            ingrediente.save()

            return JsonResponse({'sucesso': True})
    
    except Exception as e:
        print(e)
        
        return JsonResponse({'sucesso': False})

# endregion

# region Prato
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


def ModalPrato(request):
    
    ingredientes = list(Ingrediente.objects.filter(excluido=False))

    dados = {}
    
    for item in ingredientes:
        dados[item.id] = item.descricao
        
    return render(
        request,
        'Prato/ModalPrato.html',
        {
            'ingredientes': dados,
        },
    )
    
    
def AdicionarIngredientePrato(request):
    
    id = request.POST.get('id')
    index = request.POST.get('index')
    quantidade = request.POST.get('quantidade')
    
    ingrediente = Ingrediente.objects.get(pk=id)
    
    total = float(ingrediente.custo_unitario) * float(quantidade)
    
    return render(
        request,
        'Prato/ItemIngrediente.html',
        {
            'ingrediente': ingrediente,
            'index': index,
            'quantidade': quantidade,
            'total': total,
        },
    )


def SalvarPrato(request):
    
    teste = ""

    return JsonResponse({'success': True})

# endregion

# region Orcamento
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

# endregion

# region Relatorio
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

# endregion

# region Contrato
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

# endregion

def BuscarEntidadePorCpf(request):
    
    try:
        entidade = Entidade.objects.get(cpf_cnpj=request.GET.get('cpf_cnpj'))
        
        dict_entidade = {
            'nome_razao': entidade.nome_razao,
            'data_nascimento_criacao': datetime.strftime(entidade.data_nascimento_criacao, '%d/%m/%Y'),
            'cpf_cnpj': entidade.cpf_cnpj,
            'tipo': entidade.tipo,
            'excluido': entidade.excluido,
            'descricao_servico': entidade.descricao_servico,
        }
        
        convert1 = json.dumps(dict_entidade)
        #convert2 = json.dumps(entidade)
    
        return JsonResponse({'sucesso': True, 'entidade': convert1})
    
    except Exception as e:
        
        return JsonResponse({'sucesso': False})


def VerificaEntidadeExistente(request):
    
    try:
        consulta = Entidade.objects.filter(Q(cpf_cnpj=request.GET.get('cpf_cnpj')) & Q(excluido=False)).exists()
    
        return JsonResponse({'sucesso': consulta})
    
    except Exception as e:
        
        return JsonResponse({'sucesso': False})


# todo: Adicionar inclusão de telefone e e-mail
# todo: