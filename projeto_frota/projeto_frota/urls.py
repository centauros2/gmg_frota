
from django.contrib import admin
from django.urls import path, include
from app_frota import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'app_frota'

urlpatterns = [
    path('admin/', admin.site.urls),
    # rota, view responsável, nome referência
    # página inicia string vazia
    path('login/', views.login, name='login'),
    path('', views.home, name='home'),
    path('app_frota/', include('app_frota.urls')),
    # path('', views.base, name='base'),
    path('senha_reset/', views.senha_reset, name='senha_reset'),
    path('cadastro_user/', views.cadastro_user, name='cadastro_user'),
    path('cadastro_car/', views.cadastro_car, name='cadastro_car'),
    path('lista_user/', views.lista_user, name='lista_user'),
    path('lista_car/', views.lista_car, name='lista_car'),
    path('menu_opcoes/', views.menu_opcoes, name='menu_opcoes'),
    path('menu_cadastro/', views.menu_cadastro, name='menu_cadastro'),
    path('cadastro_new/', views.cadastro_new, name='cadastro_new'),
    path('opcao_car_user/', views.opcao_car_user, name='opcao_car_user'),
    path('opcao_relatorios/', views.opcao_relatorios, name='opcao_relatorios'),
    path('opcao_agendas/', views.opcao_agendas, name='opcao_agendas'),
    path('relatorio_user/', views.relatorio_user, name='relatorio_user'),
    path('relatorio_car/', views.relatorio_car, name='relatorio_car'),
    path('relatorio_empenho/', views.relatorio_empenho, name='relatorio_empenho'),
    path('locacao/', views.locacao, name='locacao'),
    path('empenho/', views.empenho, name='empenho'),
    path('volta_menu_opcoes/', views.volta_menu_opcoes, name='volta_menu_opcoes'),
    path('volta_locacao/', views.volta_locacao, name='volta_locacao'),
    path('volta_menu_cadastro/', views.volta_menu_cadastro,
         name='volta_menu_cadastro'),
    path('pag_teste/', views.pag_teste, name='pag_teste'),
    path('pesquisa_empenho/', views.pesquisa_empenho, name='pesquisa_empenho'),
    path('lista_count_motorista/', views.lista_count_motorista,
         name='lista_count_motorista'),
    path('relatorio_motorista/', views.relatorio_motorista,
         name='relatorio_motorista'),
    path('relatorio_car_empenho/', views.relatorio_car_empenho,
         name='relatorio_car_empenho'),
    path('agendas/', views.agendas, name='agendas'),
    path('resultado_agenda/', views.resultado_agenda, name='resultado_agenda'),
]
