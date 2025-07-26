from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')
    search_fields = ('title', 'short_description')