from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.


class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_no','display_image', 'father_name')
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.image.url)
        return "No Image"

    display_image.short_description = 'Image' 
    search_fields = ('name', 'email', 'phone_no')
    list_filter = ('name', 'email')

admin.site.register(Admission, AdmissionAdmin)
