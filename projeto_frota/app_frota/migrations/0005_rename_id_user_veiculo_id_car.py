# Generated by Django 5.2 on 2025-04-15 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_frota', '0004_alter_veiculo_modelo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veiculo',
            old_name='id_user',
            new_name='id_car',
        ),
    ]
