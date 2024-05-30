from django.urls import path
from . import views

app_name="dr"
urlpatterns = [
    path("", views.ChatView.as_view(), name="chat_view"), 
]