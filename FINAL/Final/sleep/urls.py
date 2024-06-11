from django.urls import path
from . import views

app_name = "sleep"
urlpatterns = [
    path('', views.video, name='video'),
    path('main/', views.main, name='main'), 
    path('define/', views.define, name='define'),
    path('team/', views.team, name='team'),
    path('clinic/', views.map, name='clinic'),
    path("video/", views.video, name="video"),
    path("bloglist/", views.bloglist, name="blist"),
    path("blogdetail/", views.blogdetail, name="bdetail"),
]