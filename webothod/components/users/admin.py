from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import (
    UserProfile,
)


class UserInline(admin.StackedInline):
    model = UserProfile


class ExtUserAdmin(UserAdmin):
    inlines = [UserInline]


admin.site.unregister(User)
admin.site.register(User, ExtUserAdmin)
