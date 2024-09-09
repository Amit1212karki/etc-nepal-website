from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *

# Create your views here.
def onGoing(request):
    on_going_project = Project.objects.filter(status='Ongoing')
    paginator = Paginator(on_going_project, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'front/pages/ongoing_projects.html', {'page_obj': page_obj})

def completed(request):
    completed_project = Project.objects.filter(status='Complete')
    paginator = Paginator(completed_project, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'front/pages/completed_projects.html', {'page_obj': page_obj})