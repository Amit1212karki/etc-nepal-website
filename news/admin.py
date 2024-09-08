from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(News)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')