from django.contrib import admin
from app_frota.models import Usuario, Veiculo

# Register your models here.
admin.site.register([Usuario, Veiculo])
