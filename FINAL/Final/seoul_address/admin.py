from django.contrib import admin
from seoul_address.models import DongID
# Register your models here.

class AdressAdmin(admin.ModelAdmin):
    list_display = (
        "address_code",
        "si_name",
        "gu_name",
        "dong_name",
        "x_cordinate",
        "y_cordinate",
    )
admin.site.register(DongID,AdressAdmin)