# Generated by Django 5.1.3 on 2024-11-06 21:32

import localflavor.br.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0004_book_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cpf',
            field=localflavor.br.models.BRCPFField(blank=True, max_length=14, null=True, unique=True, verbose_name='CPF'),
        ),
    ]
