from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    videos = Video.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'front/pages/videos.html', context )
