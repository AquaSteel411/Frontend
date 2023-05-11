import json

from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from rest_framework import viewsets
from rest_framework import permissions

from .forms import RoomForm, UserChatForm
from .serializers import ChatMessageSerializer, CustomRoomSerializer, UserSerializer
from .models import ChatMessage, CustomRoom, UserChat


class UserViewset(viewsets.ModelViewSet):
    queryset = UserChat.objects.all()
    serializer_class = UserSerializer


class ChatViewset(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer


class RoomViewset(viewsets.ModelViewSet):
    queryset = CustomRoom.objects.all()
    serializer_class = CustomRoomSerializer


class MyListRoom(ListView):
    model = CustomRoom
    ordering = '-created'
    template_name = 'chat/list_room.html'
    context_object_name = 'list_room'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_room'] = context['list_room'].filter(users__user=self.request.user.id)
        return context


class ListUsers(ListView):
    model = UserChat
    ordering = 'user'
    template_name = 'chat/list_users.html'
    context_object_name = 'list_users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_user'] = mark_safe(json.dumps(self.request.user.username))
        return context


class UserDetail(DetailView):
    model = UserChat
    template_name = 'chat/user_detail.html'
    context_object_name = 'user'


class CreateRoom(CreateView):
    form_class = RoomForm
    model = CustomRoom
    template_name = 'chat/room_edit.html'


class UpdateRoom(UpdateView):
    form_class = RoomForm
    model = CustomRoom
    template_name = 'chat/room_edit.html'


class DeleteRoom(DeleteView):
    model = CustomRoom
    template_name = 'chat/room_delete.html'
    success_url = reverse_lazy('list_room')


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, slug):
    return render(request, 'chat/room.html', {
        'slug': mark_safe(json.dumps(slug)),
        'user_name': mark_safe(json.dumps(request.user.username))
    })


def get_last_10_messages(room_name):
    chat = get_object_or_404(CustomRoom, slug=room_name.lower())
    return chat.messages.order_by('-created').all()[:10]


def get_user_author(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(UserChat, user=user)


def get_current_room(room_name, author):
    user_author = get_user_author(author)
    try:
        chat = CustomRoom.objects.get(slug=room_name.lower())
        if user_author.user.username not in set(chat.users.values_list('user__username', flat=True)):
            raise Http404('Вы не состоите в данном чате!')
    except:
        length = len(user_author.user.username)
        user_recipient = get_user_author(room_name[:-length])
        chat = CustomRoom.objects.create(name=room_name, slug=room_name)
        chat.users.add(user_author)
        chat.users.add(user_recipient)
        chat.save()
    return chat




