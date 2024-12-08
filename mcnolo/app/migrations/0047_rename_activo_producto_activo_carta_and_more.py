# Generated by Django 5.1.3 on 2024-12-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0046_producto_visibilidad"),
    ]

    operations = [
        migrations.RenameField(
            model_name="producto",
            old_name="activo",
            new_name="activo_carta",
        ),
        migrations.AddField(
            model_name="producto",
            name="activo_principal",
            field=models.BooleanField(default=True),
        ),
    ]
