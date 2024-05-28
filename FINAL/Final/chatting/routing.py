from django.urls import path

from chatting import consumers

websocket_urlpatterns = [
    path("ws/chat/<str:room_pk>/chat/", consumers.ChatConsumer.as_asgi()),
]