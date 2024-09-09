from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    images = Image.objects.prefetch_related('multiple_images').all()
    context = {
        'images': images,
    }
    return render(request, 'front/pages/image.html', context)