from django.contrib import admin

from .models import ChatMessage, CustomRoom, UserChat


admin.site.register(ChatMessage)
admin.site.register(CustomRoom)
admin.site.register(UserChat)
