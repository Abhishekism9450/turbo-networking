from django.contrib import admin
from accounts.models import UserProfile
# Register your models here.

admin.site.site_header= 'Administration'


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city')

admin.site.register(UserProfile,UserProfileAdmin)
