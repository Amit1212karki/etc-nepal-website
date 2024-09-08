from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(TeamCategory)
class TeamCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'category')
    search_fields = ('name', 'designation')
    list_filter = ('category',)