# survey/routing.py

from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/survey/$', consumers.ChatConsumer.as_asgi()),
]
