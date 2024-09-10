from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *
# Create your views here.
def index(request):
    all_news = News.objects.all()
    paginator = Paginator(all_news, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj':page_obj
    }
    return render(request,'front/pages/news.html', context)


def singlePage(request, id):
    single_news = News.objects.get(id=id)
    related_news = News.objects.exclude(id=id)[:10]

    context = {
        'single_news':single_news,
        'related_news': related_news
    }
    return render(request, 'front/pages/singlepagenews.html', context)