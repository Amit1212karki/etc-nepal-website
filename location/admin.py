from django.contrib import admin
from .models import *
# Register your models here.
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ('name',)  
    search_fields = ('name',)  

class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'province_name')  
    search_fields = ('name', 'province_name__name')
    list_filter = ('province_name',)  

class PalikaAdmin(admin.ModelAdmin):
    list_display = ('name', 'district_name')  
    search_fields = ('name', 'district_name__name', 'district_name__province_name__name')  
    list_filter = ('district_name__province_name', 'district_name')

admin.site.register(Province, ProvinceAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Palika, PalikaAdmin)