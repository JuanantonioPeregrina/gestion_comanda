# Generated by Django 4.2.17 on 2024-12-09 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_rename_activo_carta_producto_activo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='alergenos',
        ),
    ]
