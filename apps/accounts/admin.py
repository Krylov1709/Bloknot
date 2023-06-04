from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.accounts.models import User


@admin.register(User)
class MyUserAdmin(UserAdmin):
    model = User
    fieldsets = [
        ("Пользователь", {"fields": ("username", "email")}),
        ("Личные данные", {"fields": ('sex', "date_of_birth", 'is_active')})
    ]
    list_display = ['id', 'username', 'email', 'sex', "date_of_birth", 'is_active']

