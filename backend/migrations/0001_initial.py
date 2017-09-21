# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-21 12:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField(verbose_name='Data do agendamento')),
            ],
            options={
                'verbose_name_plural': 'Agendas',
            },
        ),
        migrations.CreateModel(
            name='AgendaContracts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Agenda')),
            ],
            options={
                'verbose_name_plural': 'Agendas em contrato',
            },
        ),
        migrations.CreateModel(
            name='AgendaItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_time_slot', models.TimeField(verbose_name='Hor\xe1rio Inicial')),
                ('end_time_slot', models.TimeField(verbose_name='Hor\xe1rio Final')),
                ('quantity', models.IntegerField(verbose_name='Quantidade')),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Agenda')),
            ],
            options={
                'verbose_name_plural': 'Items em Agenda',
            },
        ),
        migrations.CreateModel(
            name='AgendaResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_time_slot', models.TimeField(verbose_name='Hor\xe1rio Inicial')),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Agenda')),
            ],
            options={
                'verbose_name_plural': 'Recursos em Agenda',
            },
        ),
        migrations.CreateModel(
            name='AgendaRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_time_slot', models.TimeField(verbose_name='Hor\xe1rio Inicial')),
                ('end_time_slot', models.TimeField(verbose_name='Hor\xe1rio Final')),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Agenda')),
            ],
            options={
                'ordering': ('agenda', 'start_time_slot'),
                'verbose_name_plural': 'Salas em Agenda',
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('month', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Faturas',
            },
        ),
        migrations.CreateModel(
            name='BillStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Status de fatura',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('info', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name_plural': 'Informa\xe7\xf5es de Contato',
            },
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=10, verbose_name='Tipo')),
            ],
            options={
                'verbose_name_plural': 'Tipos de contato',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Contratos',
            },
        ),
        migrations.CreateModel(
            name='Coworking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('url', models.URLField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/logos')),
                ('cnpj', models.CharField(max_length=14)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='GenericAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=300, verbose_name='Descri\xe7\xe3o')),
            ],
            options={
                'verbose_name_plural': 'Endere\xe7os Gen\xe9ricos',
            },
        ),
        migrations.CreateModel(
            name='ImageItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/items')),
            ],
            options={
                'verbose_name_plural': 'Imagens de itens',
            },
        ),
        migrations.CreateModel(
            name='ImageResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/resources')),
            ],
            options={
                'verbose_name_plural': 'Imagens de recursos',
            },
        ),
        migrations.CreateModel(
            name='ImageRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/rooms')),
            ],
            options={
                'verbose_name_plural': 'Imagens de Salas',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.CharField(max_length=300, verbose_name='Descri\xe7\xe3o')),
                ('price', models.FloatField(default=None)),
                ('coworking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Coworking')),
            ],
            options={
                'verbose_name_plural': 'Itens',
            },
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=10, verbose_name='Tipo')),
                ('coworking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Coworking')),
            ],
            options={
                'verbose_name_plural': 'Tipos de item',
            },
        ),
        migrations.CreateModel(
            name='ItemUnity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('unity', models.CharField(max_length=10, verbose_name='Unidade')),
            ],
            options={
                'verbose_name_plural': 'Unidades de Item',
            },
        ),
        migrations.CreateModel(
            name='JuridicPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Socios  - Pessoa Juridica',
            },
        ),
        migrations.CreateModel(
            name='JuridicProfileDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='files/profiles')),
            ],
            options={
                'verbose_name_plural': 'Documentos - Pessoa Jur\xeddica',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.CharField(max_length=300, verbose_name='Descri\xe7\xe3o')),
                ('price', models.FloatField(verbose_name='Pre\xe7o')),
                ('square_meter_value', models.FloatField(default=0, verbose_name='Valor metro quadrado')),
                ('plan_type', models.BooleanField(default=True, verbose_name='Plano Din\xe2mico')),
                ('coworking', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.Coworking')),
            ],
            options={
                'verbose_name_plural': 'Planos',
            },
        ),
        migrations.CreateModel(
            name='PlanItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(verbose_name='Quantidade')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Item')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Plan')),
            ],
            options={
                'verbose_name_plural': 'Itens em Planos',
            },
        ),
        migrations.CreateModel(
            name='PlanResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity_hours', models.IntegerField(verbose_name='Quantidade de horas')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Plan')),
            ],
            options={
                'verbose_name_plural': 'Recursos em Planos',
            },
        ),
        migrations.CreateModel(
            name='PlanRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity_hours', models.IntegerField(verbose_name='Quantidade de horas')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Plan')),
            ],
            options={
                'verbose_name_plural': 'Salas em Planos',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cpf', models.CharField(max_length=11)),
                ('rg', models.CharField(max_length=13)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/profiles')),
            ],
            options={
                'verbose_name_plural': 'Perfis de Usu\xe1rios - Pessoa F\xedsica',
            },
        ),
        migrations.CreateModel(
            name='ProfileJuridic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cnpj', models.CharField(max_length=14)),
                ('juridic_name', models.CharField(max_length=300)),
                ('fantasy_name', models.CharField(max_length=300)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='images/profiles')),
            ],
            options={
                'verbose_name_plural': 'Perfis de Usu\xe1rios - Pessoa Jur\xeddica',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.CharField(max_length=300, verbose_name='Descri\xe7\xe3o')),
                ('price', models.FloatField(verbose_name='Valor')),
                ('coworking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Coworking')),
            ],
            options={
                'verbose_name_plural': 'Recursos',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.CharField(max_length=300, verbose_name='Descri\xe7\xe3o')),
                ('price_hour', models.FloatField(verbose_name='Valor Hora')),
                ('price_month', models.FloatField(verbose_name='Valor mensal')),
                ('area', models.FloatField(default=0, verbose_name='Area')),
                ('coworking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Coworking')),
            ],
            options={
                'verbose_name_plural': 'Salas',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=20, verbose_name='Tipo')),
                ('coworking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Coworking')),
            ],
            options={
                'verbose_name_plural': 'Tipos de sala',
            },
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=300, verbose_name='Descri\xe7\xe3o')),
            ],
            options={
                'verbose_name_plural': 'Endere\xe7os de Usu\xe1rios',
            },
        ),
        migrations.CreateModel(
            name='UserHasPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coworking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Coworking')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Planos e Usu\xe1rios',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.RoomType', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='profilejuridic',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.UserAddress', verbose_name='Endereco'),
        ),
        migrations.AddField(
            model_name='profilejuridic',
            name='coworking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Coworking'),
        ),
        migrations.AddField(
            model_name='profilejuridic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.UserAddress', verbose_name='Endereco'),
        ),
        migrations.AddField(
            model_name='profile',
            name='coworking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Coworking'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='planroom',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Room'),
        ),
        migrations.AddField(
            model_name='planresource',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Resource'),
        ),
        migrations.AddField(
            model_name='plan',
            name='items',
            field=models.ManyToManyField(through='backend.PlanItem', to='backend.Item', verbose_name='Itens'),
        ),
        migrations.AddField(
            model_name='plan',
            name='resources',
            field=models.ManyToManyField(through='backend.PlanResource', to='backend.Resource', verbose_name='Recursos'),
        ),
        migrations.AddField(
            model_name='plan',
            name='rooms',
            field=models.ManyToManyField(through='backend.PlanRoom', to='backend.Room', verbose_name='Salas'),
        ),
        migrations.AddField(
            model_name='juridicprofiledocument',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ProfileJuridic'),
        ),
        migrations.AddField(
            model_name='juridicpartner',
            name='juridic_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ProfileJuridic'),
        ),
        migrations.AddField(
            model_name='juridicpartner',
            name='personal_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Profile'),
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ItemType', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='item',
            name='unity',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.ItemUnity', verbose_name='Unidade'),
        ),
        migrations.AddField(
            model_name='imageroom',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Room', verbose_name='Sala'),
        ),
        migrations.AddField(
            model_name='imageresource',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Resource', verbose_name='Recurso'),
        ),
        migrations.AddField(
            model_name='imageitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Item', verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='coworking',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.GenericAddress'),
        ),
        migrations.AddField(
            model_name='contract',
            name='coworking',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.Coworking'),
        ),
        migrations.AddField(
            model_name='contract',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contacttype',
            name='coworking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Coworking'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='coworking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Coworking'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.ContactType', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='bill',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Contract'),
        ),
        migrations.AddField(
            model_name='bill',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.BillStatus'),
        ),
        migrations.AddField(
            model_name='agendaroom',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Room'),
        ),
        migrations.AddField(
            model_name='agendaresource',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Resource'),
        ),
        migrations.AddField(
            model_name='agendaitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Item'),
        ),
        migrations.AddField(
            model_name='agendacontracts',
            name='contracts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Contract'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='coworking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Coworking'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='items',
            field=models.ManyToManyField(through='backend.AgendaItem', to='backend.Item', verbose_name='Items'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='resources',
            field=models.ManyToManyField(through='backend.AgendaResource', to='backend.Resource', verbose_name='Recursos'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='rooms',
            field=models.ManyToManyField(through='backend.AgendaRoom', to='backend.Room', verbose_name='Salas'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='user_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.UserHasPlan', unique_for_date='date'),
        ),
    ]
