
from django.contrib import admin
from django.urls import path, include
from app_frota import views
from django.conf import settings
from django.conf.urls.static import static


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
    path('relatorio_user/', views.relatorio_user, name='relatorio_user'),
    path('relatorio_car/', views.relatorio_car, name='relatorio_car'),
    path('locacao/', views.locacao, name='locacao'),

]
