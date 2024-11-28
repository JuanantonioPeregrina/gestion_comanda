from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from .models import Profile, Categoria

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_migrate)
def crear_categorias_iniciales(sender, **kwargs):
    categorias = ['menu', 'carta']
    for nombre in categorias:
        Categoria.objects.get_or_create(nombre=nombre)
