# Generated by Django 5.1.3 on 2024-11-17 19:36

import app.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0031_pedido_metodo_pago"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="pedido",
            name="usuario",
            field=models.ForeignKey(
                blank=True,
                default=app.models.get_invitado_user,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]