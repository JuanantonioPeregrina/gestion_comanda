# Generated by Django 5.1.1 on 2024-10-11 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='foto',
            field=models.ImageField(default='/media/videos/fotos/perfil.webp', upload_to='perfil_fotos/'),
        ),
    ]