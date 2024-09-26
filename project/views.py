from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *

# Create your views here.
def onGoing(request):
    on_going_project = Project.objects.filter(status='Ongoing')
    paginator = Paginator(on_going_project, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'front/pages/ongoing_projects.html', {'page_obj': page_obj})


def singleOngoing(request, id):
    single_ongoing = get_object_or_404(Project, id=id)
    related_project = Project.objects.filter(status='Ongoing').exclude(id=id)[:5]

    context = {
        'single_ongoing':single_ongoing,
        'related_project':related_project
    }

    return render(request, 'front/pages/singleongoing.html', context)


def completed(request):
    completed_project = Project.objects.filter(status='Complete')
    paginator = Paginator(completed_project, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'front/pages/completed_projects.html', {'page_obj': page_obj})

def singleCompleted(request, id):
    single_completed = get_object_or_404(Project, id=id)
    related_project = Project.objects.filter(status='Complete').exclude(id=id)[:5]

    context = {
        'single_completed':single_completed,
        'related_project':related_project
    }

    return render(request, 'front/pages/singlecompleted.html', context)
