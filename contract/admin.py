from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'ocupation', 'donation_by')  # Columns to display in the admin list view
    search_fields = ('name', 'location', 'ocupation', 'donation_by')  # Fields to include in the search
    ordering = ('name',)  # Default ordering of the list

    fieldsets = (
        (None, {
            'fields': ('name', 'location', 'ocupation', 'donation_by')  # Fields to display in the admin form
        }),
    )