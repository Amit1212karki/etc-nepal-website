from django.contrib import admin
from .models import Course
from ckeditor.widgets import CKEditorWidget
from django import forms

class CourseAdminForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
        }

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    form = CourseAdminForm
    list_display = ('title', 'short_description', 'created_at', 'updated_at')
    search_fields = ('title', 'short_description')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('title', 'short_description', 'description', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
