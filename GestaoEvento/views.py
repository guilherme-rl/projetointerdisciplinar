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
            
            data = datetime.strptime(request.POST.get('data_nasc'), '%Y-%m-%d')
            
            cpf = request.POST.get('cpf_cnpj')
            cpf = re.sub(r'[^0-9]', '', cpf)
            
            novo_prestador = Entidade(
                nome_razao = request.POST.get('nome'),
                cpf_cnpj = cpf,
                data_nascimento_criacao = data,
                tipo = 'P',
            )
            novo_prestador.save()
            
            novo_prestador.endereco.create(
                cep = request.POST.get('cep') if request.POST.get('cep') else '',
                bairro = request.POST.get('bairro'),
                complemento = request.POST.get('endereco'),
                cidade = request.POST.get('cidade'),
                estado = request.POST.get('estado').upper(),
            )
            
            novo_prestador.save()

            return JsonResponse({'sucesso': True})
    
    except Exception as e:
        print(e)
        
        return JsonResponse({'sucesso': False})
        

    
def TabelaPrestador(request):
    
    prestador,= Entidade.objects.filter ((Q(tipo='P')) & Q(excluido=False))
    
    return render(
        request,
        'Prestador/Tabela.html',
        {
            'Prestador': prestador
        }
    )


def ModalNovoPrestador(request):

    return render(
        request,
        'Prestador/ModalNovo.html',
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
     
    return render(
        request,
        'ItemLocacao/ItemLocacao.html',
        {
            'title':'Itens_Locacao',
        }
    )


def TabelaItensLocacao(request):

    busca = request.POST.get('busca')     

    ItemLocacao = Entidade.objects.filter(Q(tipo='L') & Q(excluido=False))
    
    if busca:
        itemlocacao = itemlocacao.filter(descricao__icontains=busca)
    
    return render(
        request,
        'ItemLocacao/Tabela.html',
        {
            'ItemLocacao': ItemLocacao,
            'busca': busca,
        }
    )

def ModalNovoItemLocacao(request):
    
    ItemLocacao = Entidade()
    descricao = ''
    custo_unitario = ''

    return render(
        request,
        'ItemLocacao/ModalNovo.html',
        {
            'itemlocacao' : ItemLocacao,
            'descricao' : descricao,
            'custo_unitario' :custo_unitario,
        }
    
    )

def ModalExcluirItemLocacao(request):

    ItemLocacao_id = request.GET.get('id')
    ItemLocacao = Entidade.objects.get(pk=ItemLocacao_id)
    
    return render(
        request,
        'ItemLocacao/ModalExluir.html',
    {
        'ItemLocacao': ItemLocacao
    }
    )


def SalvarItemLocacao(request):   

    try:
        with transaction.atomic(): 
            itemlocacao = ItemLocacao(                
             descricao = request.POST.get('descricao'),
             custo_unitario = request.POST.get('custo_unitario'),
    
            )
             
            itemlocacao.save()
        
        return JsonResponse({'success': True})
        
    except Exception as e :
        print(e)

        return JsonResponse({'sucesso': False })

def ExcluirItemLocacao(request):

    try:
        with transaction.atomic():
            
            ItemLocacao_id = request.POST.get('id')
            ItemLocacao = Entidade.objects.get(pk=ItemLocacao_id)
           
            ItemLocacao.excluido = True

            ItemLocacao.save()
            
            return JsonResponse ({'sucesso' : True})

    except Exception as e :
        print (e)
        return JsonResponse({'sucesso' : False, 'erro' : str(e)})
    
# endregion

# region UnidadeMedida
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


def TabelaUnidadeMedida(request):
    
    busca = request.POST.get('busca')
    
    unidade_medida = UnidadeMedida.objects.all()
    
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

    return render(
        request,
        'UnidadeMedida/ModalUnidadeMedida.html',
    )


def SalvarUnidadeMedida(request):
    
    try:
        with transaction.atomic():
            unidadeMedida = UnidadeMedida(
                sigla = request.POST.get('sigla'),
                descricao = request.POST.get('descricao'),
            )
            
            unidadeMedida.save()

        return JsonResponse({'sucesso': True})
    
    except Exception as e:
        print(e)
        
        return JsonResponse({'sucesso': False})

# endregion

# region Ingrediente
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


def ModalNovoPrato(request):

    return render(
        request,
        'Prato/ModalNovo.html',
    )


def NovoPrato(request):

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