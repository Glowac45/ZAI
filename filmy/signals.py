from django.contrib.auth.models import User
from django.db import IntegrityError

from .models import Film, Ocena, ExtraInfo
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)

@receiver(post_save, sender = Film)
def nowaocena(sender, instance, created,  **kwargs):
    if created:
        Ocena.objects.create(film=instance, recenzja=instance, gwiazdki=5, owner=instance.owner)
        ExtraInfo.objects.create(film=instance, gatunek=0, czas_trwania=0, rezyser='Jan Kowalski', owner=instance.owner)
