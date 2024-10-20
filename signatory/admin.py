from django.contrib import admin
from .models import Signatory

# Register your models here.
class AdminSignatory(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ("name", "designation","institution", "created_at", "updated_at")
    
    # Fields to filter in the admin list view
    list_filter = ("designation", "created_at")
    
    # Fields to search by
    search_fields = ("name", "designation")
    
    # Fields to make editable directly in the list view
    list_editable = ("designation",)
    
    # Specify ordering
    ordering = ("-created_at",)  # Order by most recent

# Register the model with the admin class
admin.site.register(Signatory, AdminSignatory)
