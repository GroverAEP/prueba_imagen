# Generated by Django 5.2 on 2025-04-18 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba_imagenes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.CharField(max_length=255),
        ),
    ]
