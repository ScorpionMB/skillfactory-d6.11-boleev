# Generated by Django 3.1.4 on 2021-01-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20210127_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_art',
            field=models.ImageField(blank=True, upload_to='cover_book/', verbose_name='Обложка'),
        ),
    ]
