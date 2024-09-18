from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'text', 'timestamp')
    search_fields = ('sender__username', 'recipient__username', 'text')
    list_filter = ('timestamp',)

admin.site.register(User, UserAdmin)
admin.site.register(Message, MessageAdmin)

