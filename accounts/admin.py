from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.

UserModel = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserModel
    list_display = [
        'username',
        'email',
        "is_superuser",
    ]

    add_fieldsets = (
        (None, {
            "fields": (
                'email',
            ),
        }),
    ) + UserAdmin.add_fieldsets


admin.site.register(UserModel, CustomUserAdmin)
