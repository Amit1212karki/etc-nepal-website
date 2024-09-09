from django.core.paginator import Paginator
from .models import *
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

@csrf_exempt
def index(request):
    publications = Publication.objects.all()
    paginator = Paginator(publications, 6) 

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'publications': list(page_obj.object_list.values('title', 'short_description', 'pdf')),  # Adjust fields as needed
            'has_next': page_obj.has_next(),
            'has_previous': page_obj.has_previous(),
            'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
            'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None
        }
        return JsonResponse(data)
    
    return render(request, 'front/pages/publications.html', {'publications': page_obj})