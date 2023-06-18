# Generated by Django 4.2.2 on 2023-06-13 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_nombre_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(blank=True, default=100, max_length=7, verbose_name='Cantidad'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre_producto',
            field=models.CharField(blank=True, max_length=100, verbose_name='Nombre del Producto'),
        ),
    ]