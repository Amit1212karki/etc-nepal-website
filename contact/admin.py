from django.contrib import admin

from .models import *

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','subject', 'message')
    search_fields = ('name', 'email', 'phone','subject')
    list_filter = ('name', 'email')

admin.site.register(Contact, ContactAdmin)
