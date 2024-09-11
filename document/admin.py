from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'document', 'created_at', 'updated_at')
    search_fields = ('title', 'document')
    list_filter = ('created_at', 'updated_at')
