from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Usuario, Veiculo, Empenho, Acesso_Pessoa,  Acesso_Prestador, Acesso_Veiculo, Agenda
from django.template import loader, Context
from django.db.models.aggregates import Avg, Sum, Count, Min, Max
from datetime import datetime


def login(request):
    return render(request, "frota/login.html")


def modelo(request):
    return render(request, "app_frota/page/modelo.html")


def pagina1(request):
    return render(request, "app_frota/partials/pagina1.html")


def pagina2(request):
    return render(request, "app_frota/partials/pagina2.html")


def pagina3(request):
    return render(request, "app_frota/partials/pagina3.html")


def home(request):
    return render(request, "home.html")


def base(request):
    return render(request, "base.html")


def senha_reset(request):
    return render(request, "registration/senha_form_reset.html")


def cadastro_new(request):
    return render(request, "registration/register.html")

########################### * #################################


def pag_teste(request):
    logado = request.POST.get('ir_para')
    placa = request.POST.get('placa')
    data = request.POST.get('data')

    template = loader.get_template(
        'cadastro/pag_teste.html')  # página /locacao/
    context = {
        'logado': logado, 'placa': placa, 'data': data,
    }
    return HttpResponse(template.render(context, request))


def menu_cadastro(request):
    logado = request.POST.get('ir_para')
    template = loader.get_template('cadastro/menu_cadastro.html')
    context = {
        'logado': logado,
    }
    return HttpResponse(template.render(context, request))


def cadastro_car(request):
    logado = request.POST.get('ir_para')
    template = loader.get_template('cadastro/car.html')
    context = {
        'logado': logado,
    }
    return HttpResponse(template.render(context, request))


def cadastro_user(request):
    logado = request.POST.get('ir_para')
    template = loader.get_template('cadastro/user.html')
    context = {
        'logado': logado,
    }
    return HttpResponse(template.render(context, request))


def opcao_car_user(request):
    logado = request.POST.get('ir_para')
    template = loader.get_template('cadastro/opcao_car_user.html')
    context = {
        'logado': logado,
    }
    return HttpResponse(template.render(context, request))


def volta_menu_opcoes(request):
    logado = request.POST.get('ir_para')
    template = loader.get_template('cadastro/menu_opcoes.html')
    context = {
        'logado': logado,
    }
    return HttpResponse(template.render(context, request))


def volta_menu_cadastro(request):
    logado = request.POST.get('ir_para')
    template = loader.get_template('cadastro/menu_cadastro.html')
    context = {
        'logado': logado,
    }
    return HttpResponse(template.render(context, request))


def volta_locacao(request):
    logado = request.POST.get('ir_para')
    template = loader.get_template('cadastro/locacao.html')
    context = {
        'logado': logado,
    }
    return HttpResponse(template.render(context, request))


def opcao_relatorios(request):
    logado = request.POST.get('ir_para')
    template = loader.get_template('cadastro/opcao_relatorios.html')
    context = {
        'logado': logado,
    }
    return HttpResponse(template.render(context, request))


def opcao_agendas(request):
    logado = request.POST.get('ir_para')
    template = loader.get_template('cadastro/opcao_agendas.html')
    context = {
        'logado': logado,
    }
    return HttpResponse(template.render(context, request))


def empenho(request):
    logado = request.POST.get('ir_para')
    if request.method != "POST":
        return render(request, "cadastro/locacao.html", logado)
    placa = request.POST.get('placa')
    data = request.POST.get('data')
    user = Usuario.objects.filter(numero=logado).values_list()
    nome = user[0][3]
    posgra = user[0][2]
    placa = placa
    data_ini = data
    veiculo = Veiculo.objects.filter(placa=placa).values_list()
    modelo = veiculo[0][3]
    novo_empenho = Empenho()
    try:
        novo_empenho.numero = logado
        novo_empenho.posgra = posgra
        novo_empenho.nome = nome.upper()
        novo_empenho.placa = placa.upper()
        novo_empenho.modelo = modelo
        novo_empenho.data_ini = data_ini
        novo_empenho.save()
    except:
        return render(request, "cadastro/locacao.html", logado)
    empenhos = {
        'empenhos': Empenho.objects.filter(placa=placa), 'logado': str(logado),
    }
    return render(request, "cadastro/empenho.html", empenhos)


def agendas(request):
    logado = request.POST.get('ir_para')
    agenda = request.POST.get('agenda')
    titulo = []
    if request.method != "POST":
        return render(request, "cadastro/opcao_agendas.html", logado)
    if agenda == 'demandante':
        listas = list(Agenda.objects.all().values_list(
            'id_agenda', 'demandante_orgao', 'demandante_pessoa', 'local_agenda'))
        titulo.append(['Orgão', 'Demandante', 'Local'])
    if agenda == 'pessoas':
        listas = list(Acesso_Pessoa.objects.all().values_list(
            'id_pessoa', 'nome', 'pessoa_ssp', 'pessoa_cpf'))
        titulo.append(['Nome', 'Identidade', 'CPF'])
    if agenda == 'prestadores':
        listas = list(Acesso_Prestador.objects.all().values_list(
            'id_prestador', 'nome', 'pessoa_ssp', 'pessoa_cpf'))
        titulo.append(['Nome', 'Identidade', 'CPF'])
    if agenda == 'veiculos':
        listas = list(Acesso_Veiculo.objects.all().values_list(
            'id_veiculo', 'placa', 'marca', 'modelo'))
        titulo.append(['Placa', 'Marca', 'Modelo'])
    lista = []
    for dado in listas:
        lista.append([dado[0], dado[1], dado[2], dado[3]])
    resultados = lista
    pesquisa = {
        'resultados': resultados, 'logado': str(logado), 'agenda': agenda.upper(), 'titulo': titulo,
    }
    return render(request, "cadastro/agendas.html", pesquisa)


def resultado_agenda(request):
    id_nr = request.POST.get('id_nr')
    logado = request.POST.get('ir_para')
    print('@@@@', id_nr)
    if request.method != "POST":
        return render(request, "cadastro/agendas.html", logado)
    demandantes = list(Agenda.objects.filter(id_agenda=id_nr).values_list(
        'id_agenda', 'demandante_orgao', 'demandante_pessoa', 'data_agenda', 'obs_agenda', 'local_agenda'))
    pessoas = list(Acesso_Pessoa.objects.filter(
        id_pessoa=id_nr).values_list('nome', 'pessoa_ssp', 'pessoa_cpf'))
    prestadores = list(Acesso_Prestador.objects.filter(
        id_prestador=id_nr).values_list('nome', 'pessoa_ssp', 'pessoa_cpf'))
    veiculos = list(Acesso_Veiculo.objects.filter(
        id_veiculo=id_nr).values_list('placa', 'marca', 'modelo', 'cor'))
    pesquisa = {
        'logado': str(logado),
        'demandantes': demandantes,
        'pessoas': pessoas,
        'prestadores': prestadores,
    }
    return render(request, "cadastro/resultado_agenda.html", pesquisa)


def relatorio_user(request):
    logado = request.POST.get('ir_para')
    template = loader.get_template('cadastro/relatorio_user.html')
    context = {
        'logado': logado, 'usuarios': Usuario.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def relatorio_car(request):
    logado = request.POST.get('ir_para')
    template = loader.get_template('cadastro/relatorio_car.html')
    context = {
        'logado': logado, 'veiculos': Veiculo.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def pesquisa_empenho(request):
    logado = request.POST.get('ir_para')
    template = loader.get_template('cadastro/pesquisa_empenho.html')
    context = {
        'logado': logado, 'veiculos': Veiculo.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def relatorio_empenho(request):
    logado = request.POST.get('ir_para')
    if request.method != "POST":
        context = {
            'logado': logado,
        }
        return render(request, "cadastro/pesquisa_empenho.html", context, )
    empenho = Empenho.objects.all()
    dados = empenho
    total = Empenho.objects.filter().count()
    context = {
        'total': total, "empenhos": dados, 'logado': logado,
    }
    return render(request, "cadastro/relatorio_empenho.html", context, )


def relatorio_car_empenho(request):
    logado = request.POST.get('ir_para')
    if request.method != "POST":
        context = {
            'logado': logado,
        }
        return render(request, "cadastro/pesquisa_car_empenho.html", context, )
    dados = Empenho.objects.filter().values_list('placa', flat=True)
    veiculos = Veiculo.objects.filter(placa__in=dados)
    context = {
        "veiculos": veiculos, 'logado': logado,
    }
    return render(request, "cadastro/relatorio_car_empenho.html", context, )


def locacao(request):
    if request.method != "POST":
        return HttpResponse(template.render(context, request))
    placa = request.POST.get('placa')
    marca = request.POST.get('marca')
    modelo = request.POST.get('modelo')
    cor = request.POST.get('cor')
    combustivel = request.POST.get('combustivel')
    data = request.POST.get('data')
    logado = request.POST.get('ir_para')
    if data == "":
        template = loader.get_template('cadastro/locacao.html')
        context = {
            'logado': logado,
        }
        return HttpResponse(template.render(context, request))
    empenhados = Empenho.objects.filter(
        data_ini=data).values_list('placa', flat=True)  # aqui ###########
    localizados = Veiculo.objects.filter().exclude(placa__in=empenhados)
    if placa != "":
        localizados = localizados.filter(placa=placa)
        template = loader.get_template('cadastro/locacao.html')
        context = {
            'localizados': localizados, 'logado': logado, 'data': data,
        }
        return HttpResponse(template.render(context, request))
    # localizados = Veiculo.objects.filter().exclude(data=data)  # all type = None
    if marca is not None:
        localizados = localizados.filter(marca=marca)
    if modelo is not None:
        localizados = localizados.filter(modelo=modelo)
    if cor is not None:
        localizados = localizados.filter(cor=cor)
    if combustivel is not None:
        localizados = localizados.filter(combustivel=combustivel)
    template = loader.get_template('cadastro/locacao.html')
    context = {
        'localizados': localizados, 'logado': logado, 'data': data,
    }
    return HttpResponse(template.render(context, request))


def lista_user(request):
    logado = request.POST.get('ir_para')
    if request.method == "POST":
        novo_user = Usuario()
        try:
            nr = str(request.POST.get('numero'))
            novo_user.numero = int(nr[0:7])
            novo_user.posgra = request.POST.get('posgra')
            novo_user.nome = request.POST.get('nome').upper()
            novo_user.cnhcat = request.POST.get('cnhcat')
            novo_user.funcao = request.POST.get('funcao')
            novo_user.senha = request.POST.get('senha')
            novo_user.save()
        except:
            msg_erro = {
                'msg_erro': 'ERRO: Servidor já foi cadastrado!', 'logado': logado,
            }
            return render(request, "cadastro/user.html", msg_erro)
        else:
            template = loader.get_template(
                'cadastro/lista_user.html')  # locacao
            usuarios = Usuario.objects.all()
            return HttpResponse(template.render({'usuarios': usuarios, 'logado': logado}, request))
    else:
        usuarios = {
            'logado': logado,
        }
        return render(request, "cadastro/lista_user.html", logado)


def lista_car(request):
    logado = request.POST.get('ir_para')
    if request.method == "POST":
        novo_car = Veiculo()
        try:
            novo_car.placa = request.POST.get('placa').upper()
            novo_car.marca = request.POST.get('marca')
            novo_car.modelo = request.POST.get('modelo')
            novo_car.cor = request.POST.get('cor')
            novo_car.combustivel = request.POST.get('combustivel')
            novo_car.data = datetime.now()
            novo_car.save()
        except:
            msg_erro = {
                'msg_erro': 'ERRO: Placa de veículo já foi cadastrada!', 'logado': logado,
            }
            return render(request, "cadastro/car.html", msg_erro)
        else:
            veiculos = Veiculo.objects.all()
            return render(request, "cadastro/lista_car.html", {'veiculos': veiculos, 'logado': logado})
    else:
        return render(request, "cadastro/car.html")


def menu_opcoes(request):
    if request.method == "GET":
        return render(request, "cadastro/menu_opcoes.html")
    else:
        user_nr = request.POST.get('user_nr')
        password = request.POST.get('password')
        user = Usuario.objects.filter(numero=user_nr).values_list()
        if user:
            if user[0][6] == password:
                logado = user[0][1]
                template = loader.get_template('cadastro/menu_opcoes.html')
                context = {
                    'logado': logado,
                }
                return HttpResponse(template.render(context, request))
            else:
                template = loader.get_template("frota/login.html")
                context = {
                    'erro': 'Número ou senha errados!',
                }
                return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template("frota/login.html")
            context = {
                'erro': 'Número ou senha errados!',
            }
            return HttpResponse(template.render(context, request))


def lista_count_motorista(request):
    logado = request.POST.get('ir_para')
    if request.method != "POST":
        context = {
            'logado': logado,
        }
        return render(request, "cadastro/pesquisa_empenho.html", context, )
    empenho = Empenho.objects.all()
    # dados = empenho.all().aggregate(Total=Count('numero'))
    dados = empenho.values('posgra', 'nome').annotate(Empenhos=Count('numero'))
    media = dados.aggregate(Media=Avg('Empenhos'))
    total = Empenho.objects.filter().count()
    # user = Empenho.objects.aggregate(count('numero'))
    # veiculo = Veiculo.objects.filter(numero='1078914').count()
    context = {
        'total': total, "empenhos": dados, "media": media, 'logado': logado,
    }
    return render(request, "cadastro/relatorio_empenho.html", context, )


def relatorio_motorista(request):
    logado = request.POST.get('ir_para')
    if request.method != "POST":
        context = {
            'logado': logado,
        }
        return render(request, "cadastro/pesquisa_empenho.html", context, )
    empenho = Empenho.objects.all()
    # dados = empenho.all().aggregate(Total=Count('numero'))
    dados = empenho.values('posgra', 'nome').annotate(Empenhos=Count('numero'))
    media = dados.aggregate(Media=Avg('Empenhos'))
    total = Empenho.objects.filter().count()
    # user = Empenho.objects.aggregate(count('numero'))
    # veiculo = Veiculo.objects.filter(numero='1078914').count()
    context = {
        'total': total, "empenhos": dados, "media": media, 'logado': logado,
    }
    return render(request, "cadastro/relatorio_motorista.html", context, )
