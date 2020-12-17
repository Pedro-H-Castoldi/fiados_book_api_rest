# Generated by Django 2.2.17 on 2020-12-16 18:01

import cpf_field.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('full_name', models.CharField(max_length=100, verbose_name='Nome completo')),
                ('date_of_birth', models.DateField(verbose_name='Data de nascimento')),
                ('sex', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino')], max_length=9, verbose_name='Sexo')),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31, verbose_name='Telefone')),
                ('email', models.EmailField(default='', max_length=254, unique=True, verbose_name='E-mail')),
                ('cpf', cpf_field.models.CPFField(max_length=14, unique=True, verbose_name='CPF')),
                ('indebted', models.BooleanField(default=False, verbose_name='Devendo?')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('product', models.CharField(max_length=100, verbose_name='produto')),
                ('type', models.CharField(choices=[('household_appliance', 'Eletrodoméstico'), ('electronic', 'Eletrônico'), ('food', 'Alimento'), ('clean', 'Limpeza'), ('beauty', 'Beleza'), ('clothing', 'Vestuário'), ('intimate_care', 'Cuidado íntimo'), ('varied', 'Variados')], max_length=20, verbose_name='Tipo')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('amount', models.IntegerField(verbose_name='Quantidade')),
                ('image', stdimage.models.StdImageField(upload_to='', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
                ('purchase_type', models.BooleanField(default=False, verbose_name='Fiado?')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cliente', to='core.Client')),
                ('product', models.ManyToManyField(blank=True, related_name='products', to='core.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Venda',
                'verbose_name_plural': 'Vendas',
                'ordering': ['id'],
            },
        ),
    ]