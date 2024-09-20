from django.contrib import admin
from .models import SuccessHistory

# Register your models here.

@admin.register(SuccessHistory)
class SuccessHistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'number', 'suffix', 'is_active')
    search_fields = ('name','creatted_at')
    list_filter = ('created_at', 'updated_at')