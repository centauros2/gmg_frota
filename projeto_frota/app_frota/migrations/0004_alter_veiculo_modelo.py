# Generated by Django 5.2 on 2025-04-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_frota', '0003_veiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='modelo',
            field=models.TextField(max_length=50),
        ),
    ]
