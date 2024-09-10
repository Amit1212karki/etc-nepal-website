from django.shortcuts import render , get_object_or_404
from .models import *


# Create your views here.

def index(request):
    images = Image.objects.all()
    context = {
        'images': images,
    }
    return render(request, 'front/pages/image.html', context)
    

def singlePageImage(request, id):
    single_image = get_object_or_404(Image, id=id)

    related_images = Images.objects.filter(image=single_image)[:5]

    context = {
        'single_image': single_image,
        'related_images': related_images,
    }
    return render(request, 'front/pages/singleimage.html', context)