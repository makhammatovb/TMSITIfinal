# Generated by Django 5.0.4 on 2024-05-08 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='appeal_description',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='type',
        ),
    ]
