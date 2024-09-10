from django.shortcuts import render
from notice.models import *
from project.models import *
from news.models import *


def index(request):
    home_notice = Notice.objects.all()
    home_project_ongoing = Project.objects.filter(status='Ongoing')[:3]
    home_project_completed = Project.objects.filter(status='Complete')[:3]
    home_news = News.objects.all()[:4]

    context = {
        'notice':home_notice,
        'project_ongoing': home_project_ongoing,
        'project_completed': home_project_completed,
        'news':home_news
    }
    return render(request,'front/pages/homepage.html', context)

def about(request):
    return render(request, 'front/pages/about.html')