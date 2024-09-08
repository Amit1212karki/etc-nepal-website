from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video')  # Customize the fields displayed in the list view
    search_fields = ('title',) 
