from django.contrib import admin
from chatting.models import Room, RoomMember


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(RoomMember)
class RoomMemberAdmin(admin.ModelAdmin):
    pass