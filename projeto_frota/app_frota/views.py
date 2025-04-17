from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Usuario, Veiculo
from django.template import loader, Context
from django.db import IntegrityError


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


def menu_opcoes(request):
    return render(request, "cadastro/menu_opcoes.html")


def menu_cadastro(request):
    return render(request, "cadastro/menu_cadastro.html")


def cadastro_car(request):
    return render(request, "cadastro/car.html")


def cadastro_user(request):
    return render(request, "cadastro/user.html")


def base(request):
    return render(request, "base.html")


def senha_reset(request):
    return render(request, "registration/senha_form_reset.html")


def cadastro_new(request):
    return render(request, "registration/register.html")


def opcao_car_user(request):
    return render(request, "cadastro/opcao_car_user.html")


def opcao_relatorios(request):
    return render(request, "cadastro/opcao_relatorios.html")


def relatorio_user(request):
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, "cadastro/relatorio_user.html", usuarios)


def relatorio_car(request):
    veiculos = {
        'veiculos': Veiculo.objects.all()
    }
    return render(request, "cadastro/relatorio_car.html", veiculos)


def locacao(request):
    placa = request.POST.get('placa')
    marca = request.POST.get('marca')
    modelo = request.POST.get('modelo')
    cor = request.POST.get('cor')
    combustivel = request.POST.get('combustivel')
    data = request.POST.get('data')
    if data == "":
        # return render(request, "cadastro/locacao.html")
        template = loader.get_template('cadastro/locacao.html')
        return HttpResponse(template.render(request))
    else:
        if placa != "":  # typer= str
            localizados = Veiculo.objects.filter(
                placa=placa).exclude(data=data)
            template = loader.get_template('cadastro/locacao.html')
            context = {
                'localizados': localizados,
            }
            return HttpResponse(template.render(context, request))
        else:
            localizados = Veiculo.objects.filter().exclude(data=data)  # all type = None
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
                'localizados': localizados,
            }
            return HttpResponse(template.render(context, request))


def lista_user(request):
    if request.method == "POST":
        novo_user = Usuario()
        try:
            novo_user.numero = request.POST.get('numero')
            novo_user.posgra = request.POST.get('posgra')
            novo_user.nome = request.POST.get('nome').upper()
            novo_user.cnhcat = request.POST.get('cnhcat')
            novo_user.funcao = request.POST.get('funcao')
            novo_user.senha = request.POST.get('senha')
            novo_user.save()
        except:
            msg_erro = {
                'msg_erro': 'ERRO: Servidor já cadastrado!',
            }
            return render(request, "cadastro/user.html", msg_erro)
        else:
            usuarios = {
                'usuarios': Usuario.objects.all()
            }
            # retornar para para lista_user
            return render(request, "cadastro/lista_user.html", usuarios)
    else:
        return render(request, "cadastro/user.html")


def lista_car(request):
    if request.method == "POST":
        novo_car = Veiculo()
        try:
            novo_car.placa = request.POST.get('placa').upper()
            novo_car.marca = request.POST.get('marca')
            novo_car.modelo = request.POST.get('modelo')
            novo_car.cor = request.POST.get('cor')
            novo_car.combustivel = request.POST.get('combustivel')
            novo_car.data = request.POST.get('data')
            novo_car.save()
        except:
            msg_erro = {
                'msg_erro': 'ERRO: Placa de veículo já cadastrada!',
            }
            return render(request, "cadastro/car.html", msg_erro)
        else:
            veiculos = {
                'veiculos': Veiculo.objects.all()
            }
            # retornar para para lista_user
            return render(request, "cadastro/lista_car.html", veiculos)
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
                nome = user[0][3]
                template = loader.get_template('cadastro/menu_opcoes.html')
                context = {
                    'firstname': nome,
                }
                return HttpResponse(template.render(context, request))

                # return render(request, "frota/menu_opcoes.html", texto)
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
