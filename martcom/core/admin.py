from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "city",
                    "state",
                    "address",
                    "mobile",
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
