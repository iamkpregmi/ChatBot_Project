from django.contrib import admin
from .models import UserQuery

class UserQueryAdmin(admin.ModelAdmin):
    fields = ['query', 'response', 'timestamp']
    search_fields = ['query', 'response']

admin.site.register(UserQuery,UserQueryAdmin)

