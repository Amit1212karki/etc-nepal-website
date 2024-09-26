from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
# Create your views here.

# Create your views here.
def index(request):
    all_course = Course.objects.all()
    paginator = Paginator(all_course, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj
    }
    return render(request,'front/pages/course.html', context)


def singlePage(request, id):
    single_course = Course.objects.get(id=id)
    related_course = Course.objects.exclude(id=id)[:10]

    context = {
        'single_course':single_course,
        'related_course': related_course
    }
    return render(request, 'front/pages/singlepagecourse.html', context)
