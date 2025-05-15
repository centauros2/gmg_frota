from django.urls import path
from app_frota import views


app_name = 'app_frota'

urlpatterns = [
    # path('app_frota/', views.app_frota, name='app_frota'),
    path('modelo/', views.modelo),
    path('pagina1/', views.pagina1),
    path('pagina2/', views.pagina2),
    path('pagina3/', views.pagina3),
]
