from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from web.models.user import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ("user",)
