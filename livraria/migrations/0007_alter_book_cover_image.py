# Generated by Django 5.1.3 on 2024-11-06 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0006_alter_customer_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/%Y/%m/%d/', verbose_name='Imagem de Capa'),
        ),
    ]