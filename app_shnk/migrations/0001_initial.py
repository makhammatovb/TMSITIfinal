# Generated by Django 5.0.4 on 2024-05-15 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SHNKGroupsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.IntegerField()),
                ('group_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'SHNK Group',
                'verbose_name_plural': 'SHNK Groups',
                'db_table': 'shnk_groups',
            },
        ),
        migrations.CreateModel(
            name='SHNKSystemsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_number', models.IntegerField()),
                ('system_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'SHNK System',
                'verbose_name_plural': 'SHNK Systems',
                'db_table': 'shnk_systems',
            },
        ),
        migrations.CreateModel(
            name='SHNKSubSystemsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsystem_code', models.CharField(max_length=25)),
                ('subsystem_name', models.CharField(max_length=255)),
                ('subsystem_file_uz', models.FileField(upload_to='subsystems_uz')),
                ('subsystem_file_ru', models.FileField(upload_to='subsystems_ru')),
                ('subsystem_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shnk.shnkgroupsmodel')),
            ],
            options={
                'verbose_name': 'SHNK Subsystem',
                'verbose_name_plural': 'SHNK Subsystems',
                'db_table': 'shnk_subsystems',
            },
        ),
        migrations.AddField(
            model_name='shnkgroupsmodel',
            name='group_system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_shnk.shnksystemsmodel'),
        ),
    ]