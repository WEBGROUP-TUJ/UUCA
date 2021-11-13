from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import UserSettings
from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class UserSettingsInlines(admin.StackedInline):
    model = UserSettings
    can_delete = False
    verbose_name_plural = 'Settings'


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', ]
    inlines = [UserSettingsInlines, ]


admin.site.register(CustomUser, CustomUserAdmin)
