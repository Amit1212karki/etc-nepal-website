from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.
def index(request):
    search_query = request.GET.get('search', '')
    all_documents = Document.objects.filter(
        Q(title__icontains=search_query)
    ) if search_query else Document.objects.all()

    paginator = Paginator(all_documents, 6)
    page_number = request.GET.get('page', 1)
    documents = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'documents': list(documents.object_list.values('title', 'document')),  
            'has_next': documents.has_next(),
            'has_previous': documents.has_previous(),
            'next_page_number': documents.next_page_number() if documents.has_next() else None,
            'previous_page_number': documents.previous_page_number() if documents.has_previous() else None
        }
        return JsonResponse(data)

    return render(request, 'front/pages/documents.html', {'all_documents': documents})
