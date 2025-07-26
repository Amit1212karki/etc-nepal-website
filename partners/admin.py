from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name','image','created_at')
    search_fields = ('name','creatted_at')
    list_filter = ('created_at', 'updated_at')
