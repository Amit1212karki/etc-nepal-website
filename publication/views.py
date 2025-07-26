from django.core.paginator import Paginator
from .models import *
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

@csrf_exempt
def index(request):
    search_query = request.GET.get('search', '')  # Get search query from GET request
    publications = Publication.objects.filter(
        Q(title__icontains=search_query) | Q(short_description__icontains=search_query)
    ) if search_query else Publication.objects.all()  # Filter by search query if present

    paginator = Paginator(publications, 6)  # 6 items per page
    page_number = request.GET.get('page', 1)  # Get page number from GET request
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'publications': list(page_obj.object_list.values('title', 'short_description', 'pdf')),
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
            'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
            'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None
        }
        return JsonResponse(data)
    
    return render(request, 'front/pages/publications.html', {'publications': page_obj})
