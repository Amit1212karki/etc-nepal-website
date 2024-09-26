from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    link = Video.objects.all()
    context = {
        'link': link
    }
    return render(request, 'front/pages/videos.html', context )
