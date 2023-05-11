from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

from .models import UserChat, CustomRoom


@receiver(post_save, sender=User)
def create_author(sender, instance, created, **kwargs):
    if created:
        UserChat.objects.create(user=instance)


@receiver(pre_save, sender=CustomRoom)
def populate_slug(sender, instance, **kwargs):
    instance.slug = slugify(instance.name)

