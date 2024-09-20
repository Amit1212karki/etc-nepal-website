from django.contrib import admin

# Register your models here.
from .models import *
from django.utils.html import mark_safe

class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'background_image_display', 'qr_code_display')

    def background_image_display(self, obj):
        if obj.background_image:
            return mark_safe(f'<img src="{obj.background_image.url}" width="100" height="100" />')
        return "No background image"

    background_image_display.short_description = 'Background Image'

    def qr_code_display(self, obj):
        if obj.qr_code_image:
            qr_code_img = f'<a href="{obj.qr_code_image.url}" download><img src="{obj.qr_code_image.url}" width="100" height="100" style="cursor: pointer;" /></a>'
            download_link = f'<a href="{obj.qr_code_image.url}" download>Download QR Code</a>'
            return mark_safe(f'{qr_code_img}<br>{download_link}')
        return "No QR code image"

    qr_code_display.short_description = 'QR Code Image'

admin.site.register(Certificate, CertificateAdmin)
