from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path('list/', views.index, name='list'),
    path('<int:pk>/', views.detail, name='detail'),
]

