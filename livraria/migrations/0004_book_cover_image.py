# Generated by Django 5.1.3 on 2024-11-06 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livraria', '0003_alter_author_bio_alter_author_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='book_covers/', verbose_name='Imagem de Capa'),
        ),
    ]
