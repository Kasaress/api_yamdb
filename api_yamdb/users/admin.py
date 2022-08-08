from django.contrib import admin

from .models import CustomUser


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'role')


admin.site.register(CustomUser, UserAdmin)
