from django.urls import path
from . import views

app_name = "dr"
urlpatterns = [
    path("drai/", views.sleep_clinic_room_detail, name="drai"),
    path("list/", views.list, name="list"),
]
