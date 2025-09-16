from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "is_approved", "is_staff"]
    list_filter = ["is_approved", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("is_approved",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("is_approved",)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)