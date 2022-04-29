from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, HappinessInfo

admin.site.register(User, UserAdmin)


class InfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'happiness_level']


admin.site.register(HappinessInfo, InfoAdmin)
