from django.urls import path
from chatting import views

urlpatterns = [
    path("chat/", views.chat_page),
]