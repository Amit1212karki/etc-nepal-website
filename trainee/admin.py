from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Trainee)
class TraineeAdmin(admin.ModelAdmin):
    list_display = ('name', 'occupation', 'gender', 'marital_status', 'date_of_birth_ad', 'is_selected')
    list_filter = ('gender', 'marital_status', 'province', 'district', 'palika', 'batch')
    search_fields = ('name', 'occupation', 'citizenship_no', 'email')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'occupation', 'gender', 'marital_status', 'date_of_birth_ad', 'date_of_birth_bs')
        }),
        ('Contact Information', {
            'fields': ('phone_no', 'email', 'citizenship_no', 'issue_date', 'issue_district', 'mother_name', 'father_name')
        }),
        ('Images', {
            'fields': ('citizenship_front_image', 'citizenship_back_image', 'image')
        }),
        ('Foreign Keys', {
            'fields': ('contract', 'batch', 'province', 'district', 'palika')
        }),
        ('Selection Status', {
            'fields': ('is_selected',)
        }),
    )
    