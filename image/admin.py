from django.contrib import admin
from .models import *
# Register your models here.
class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1  # Number of extra forms to display for adding images


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')
    inlines = [ImagesInline]  # Adds the inline model for multiple images

# Registering the Images model separately
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('image', 'images')