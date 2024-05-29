from django.urls import path
from . import views

app_name = "sleep"
urlpatterns = [
    path('', views.video, name='video'),
    path('main/', views.main, name='main'), 
    path('define/', views.define, name='define'),
    path('chatbot/', views.chatbot, name='chatbot'),
    # path('chatting/', views.chatting, name='chatting'),
    path('drai/', views.drai, name='dr_ai'),
    path('result/', views.result, name='result'),
    path('team/', views.team, name='team'),
    path('clinic/', views.map, name='clinic'),
    path("video/", views.video, name="video"),
    
    # path("1/", views.list_answer),
]