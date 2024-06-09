from django.urls import path
from . import views

app_name = "dr"
urlpatterns = [
    path("drai/", views.chat_room, name="drai"),
    path("list/", views.dr_list, name="list"),
    path("draitest/", views.chat_room_test, name="draitest"),
]