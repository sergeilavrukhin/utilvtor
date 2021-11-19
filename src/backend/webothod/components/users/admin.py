from django.contrib import admin
from django.contrib.auth.models import User
from .models import (
    UserProfile,
)


class UserInline(admin.StackedInline):
    model = UserProfile


class UserAdmin(admin.ModelAdmin):
    inlines = [UserInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
