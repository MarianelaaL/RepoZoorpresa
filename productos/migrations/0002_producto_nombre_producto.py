# Generated by Django 4.2.2 on 2023-06-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='nombre_producto',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nombre_Producto'),
        ),
    ]
