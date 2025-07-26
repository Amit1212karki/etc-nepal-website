from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'partner', 'project_location', 'project_duration', 'status')
    search_fields = ('title', 'partner', 'project_location')
    list_filter = ('status', 'project_location')