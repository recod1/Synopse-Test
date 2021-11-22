# Generated by Django 3.2.6 on 2021-11-19 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameGroup', models.CharField(max_length=80, verbose_name='Название группы')),
                ('configFile', models.FileField(upload_to='files/', verbose_name='Файл конфигурации для группы')),
                ('loginGroup', models.CharField(max_length=30, verbose_name='Логин для микротиков, принадлежащих этой группе')),
                ('passGroup', models.CharField(max_length=30, verbose_name='Пароль для микротиков, принадлежащих этой группе')),
            ],
            options={
                'verbose_name': 'Группу',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameGroup', models.CharField(max_length=80, verbose_name='Название подгруппы')),
                ('configFile', models.FileField(upload_to='files/', verbose_name='Файл конфигурации для подгруппы')),
                ('loginGroup', models.CharField(max_length=30, verbose_name='Логин для микротиков, принадлежащих этой подгруппе')),
                ('passGroup', models.CharField(max_length=30, verbose_name='Пароль для микротиков, принадлежащих этой подгруппе')),
                ('belongGroupGlobal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.globalgroup', verbose_name='группы')),
            ],
            options={
                'verbose_name': 'Подгруппу',
                'verbose_name_plural': 'Подгруппы',
            },
        ),
        migrations.CreateModel(
            name='Mikrot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mikrotIP', models.CharField(max_length=20, verbose_name='Адрес Микротик')),
                ('mikrotName', models.CharField(max_length=30, verbose_name='Имя Микротик')),
                ('mikrotLogin', models.CharField(max_length=30, verbose_name='Логин Микротик')),
                ('mikrotPass', models.CharField(max_length=30, verbose_name='Пароль Микротик')),
                ('belongGroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.group', verbose_name='подгруппы')),
                ('belongGroupGlobal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.globalgroup', verbose_name='группы')),
            ],
            options={
                'verbose_name': 'Микротик',
                'verbose_name_plural': 'Микротики',
            },
        ),
    ]
