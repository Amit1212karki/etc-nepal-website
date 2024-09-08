from django.core.paginator import Paginator
from .models import *
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    search_query = request.GET.get('search', '')
    publications = Publication.objects.filter(title__icontains=search_query)
    
    paginator = Paginator(publications, 5)  # Show 5 publications per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'publications': page_obj,
        'search_query': search_query,
    }

    return render(request, 'front/pages/publications.html', context)

@csrf_exempt
def publication_list(request):
    if request.method == 'POST':
        search_query = request.POST.get('search', '')
        publications = Publication.objects.filter(title__icontains=search_query)
        
        paginator = Paginator(publications, 5)  # Show 5 publications per page
        page_number = request.POST.get('page', 1)  # Default to the first page
        page_obj = paginator.get_page(page_number)
        
        publication_list = list(page_obj.object_list.values('title', 'id'))
        
        return JsonResponse({
            'publications': publication_list,
            'page_number': page_obj.number,
            'num_pages': paginator.num_pages,
            'has_previous': page_obj.has_previous(),
            'has_next': page_obj.has_next(),
        })
    return JsonResponse({'error': 'Invalid request method'}, status=405)