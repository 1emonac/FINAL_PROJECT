from django.urls import path
from . import views

app_name = "dr"
urlpatterns = [
    path("drai/", views.chat_room, name="drai"),
    path("list/", views.list, name="list"),
]
