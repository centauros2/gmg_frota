# Generated by Django 5.2 on 2025-04-15 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_frota', '0002_usuario_delete_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.TextField(max_length=50)),
                ('marca', models.TextField(max_length=100)),
                ('modelo', models.TextField(max_length=5)),
                ('cor', models.TextField(max_length=10)),
                ('combustivel', models.TextField(max_length=50)),
            ],
        ),
    ]
