from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("login2/", views.login_view2, name="login2"),
    path('logout/', views.logout_view, name='logout'),
    path("signup/", views.signup, name="signup"),
    path("signout/", views.signout, name="signout"),
    path("profile/", views.profile, name="profile"),
]