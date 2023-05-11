import re

from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.urls import reverse


class UserChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', blank=True)
    avatar = models.ImageField(default='/anonim.jpg')

    def __str__(self):
        return self.user.username

    @property
    def image_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url


class ChatMessage(models.Model):
    author = models.ForeignKey(UserChat, on_delete=models.CASCADE)
    text = models.TextField(max_length=2048)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class CustomRoom(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(UserChat, related_name='users')
    messages = models.ManyToManyField(ChatMessage, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list_room')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
