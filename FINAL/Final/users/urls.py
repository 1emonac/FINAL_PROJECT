from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("login2/", views.login_view2, name="login2"),
    path('logout/', views.logout_view, name='logout'),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile")
]