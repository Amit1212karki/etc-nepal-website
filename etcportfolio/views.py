import datetime
from django.shortcuts import render
from etcportfolio import renderers
from notice.models import *
from project.models import *
from news.models import *
from partners.models import *
from records.models import *
from course.models import *
from django.template.loader import get_template



def index(request):
    home_notice = Notice.objects.all()
    home_project_ongoing = Project.objects.filter(status='Ongoing')[:3]
    home_project_completed = Project.objects.filter(status='Complete')[:3]
    home_news = News.objects.all()[:4]
    home_partner = Partner.objects.all()
    home_items = SuccessHistory.objects.filter(is_active=True)
    home_course = Course.objects.all()[:4]

    context = {
        'notice':home_notice,
        'project_ongoing': home_project_ongoing,
        'project_completed': home_project_completed,
        'news':home_news,
        'partner':home_partner,
        'success_items':home_items,
        'home_course':home_course
    }
    return render(request,'front/pages/homepage.html', context)

def about(request):
    return render(request, 'front/pages/about.html')


def vission(request):
    return render(request, 'front/pages/vission.html')

def mission(request):
    return render(request, 'front/pages/mission.html')

def goal(request):
    return render(request, 'front/pages/goal.html')

def hrDiagram(request):
    return render(request, 'front/pages/hrdiagram.html')

def objective(request):
    return render(request, 'front/pages/objective.html')

def pdf_view(request, *args, **kwargs):
    data = {
        
    }
    
    
    return renderers.render_to_pdf_pdfkit('pdfs/certificate/index.html', data)