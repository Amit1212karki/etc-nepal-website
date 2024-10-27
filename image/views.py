from django.shortcuts import render , get_object_or_404
from .models import *
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    images = Image.objects.all()
    all_iamges = Paginator(images, 6)
    page_number = request.GET.get('page')
    paginate_images = all_iamges.get_page(page_number)
    context = {
        'images': paginate_images,
    }
    return render(request, 'front/pages/image.html', context)
    

def singlePageImage(request, id):
    single_image = get_object_or_404(Image, id=id)
    related_images = Image.objects.exclude(id=id).order_by('-created_at')[:5]

    context = {
        'single_image': single_image,
        'related_images': related_images,
    }
    return render(request, 'front/pages/singleimage.html', context)