# Generated by Django 5.1.1 on 2024-10-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_pedido_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='productos',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='disponible',
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(default='Sin descripción'),
        ),
    ]
