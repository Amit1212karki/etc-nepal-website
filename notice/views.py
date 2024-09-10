from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    all_notice = Notice.objects.all()

    context = {
        'all_notice':all_notice
    }
    return render(request,'front/pages/notice.html', context)