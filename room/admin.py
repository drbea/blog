from django.contrib import admin

from .models import Room, Topic, Message
# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass
