from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'qualification', 'tot')
    search_fields = ('name', 'qualification')