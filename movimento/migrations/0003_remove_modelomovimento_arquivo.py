# Generated by Django 4.0.3 on 2022-05-20 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimento', '0002_modelomovimento_arquivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelomovimento',
            name='arquivo',
        ),
    ]