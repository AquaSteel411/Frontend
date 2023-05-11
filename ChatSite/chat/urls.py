from django.urls import path

from . import views
from .views import CreateRoom, MyListRoom, ListUsers, DeleteRoom, UpdateRoom, UserDetail, UserChatUpdate

urlpatterns = [
    path('', views.index, name='index'),
    path('list_room/<slug:slug>/', views.room, name='room'),
    path('create_room/', CreateRoom.as_view(), name='create_room'),
    path('list_room/', MyListRoom.as_view(), name='list_room'),
    path('list_users', ListUsers.as_view(), name='list_users'),
    path('list_room/<slug:slug>/update_room', UpdateRoom.as_view(), name='update_room'),
    path('list_room/<slug:slug>/delete_room', DeleteRoom.as_view(), name='delete_room'),
    path('list_users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
]
