from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {"fields" : ("username", "password")}),
        ("개인정보", {"fields": ("email",)}),
        ("권한", {"fields": ("is_active", "is_staff", "is_superuser")}),
    ]