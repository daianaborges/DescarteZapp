# Generated by Django 3.2.8 on 2021-11-12 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doadores',
            name='celular',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='doadores',
            name='telefonefixo',
            field=models.CharField(max_length=20, unique=True, verbose_name='Telefone Fixo'),
        ),
    ]
