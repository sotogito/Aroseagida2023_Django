from django.contrib import admin
from .models import AddUserProfile

class AddUserProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'birthdate', 'user_unique_id']
    search_fields = ['user']

admin.site.register(AddUserProfile, AddUserProfileAdmin)
