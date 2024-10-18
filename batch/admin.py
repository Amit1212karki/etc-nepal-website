from django.contrib import admin
from .models import Batch
from trainer.models import Trainer 
# Register your models here.
@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'start_date', 'seats')
    search_fields = ('name', 'duration')