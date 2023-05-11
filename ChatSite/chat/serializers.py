from django.contrib.auth.models import User

from .models import ChatMessage, CustomRoom, UserChat
from rest_framework import serializers


class ChatMessageSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects)

    class Meta:
        model = ChatMessage
        fields = ['id', 'text', 'user']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', queryset=User.objects)

    class Meta:
        model = UserChat
        fields = ['id', 'user']


class CustomRoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomRoom
        fields = ['id', 'name', 'users', 'messages']


