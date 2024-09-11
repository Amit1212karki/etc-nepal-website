from django.shortcuts import render
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.
def index(request):
    search_query = request.GET.get('search', '')
    all_notices = Notice.objects.filter(
        Q(title__icontains=search_query) | Q(description__icontains=search_query)
    ) if search_query else Notice.objects.all()

    paginator = Paginator(all_notices, 6)
    page_number = request.GET.get('page', 1)
    notices = paginator.get_page(page_number)

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'notices': list(notices.object_list.values('title', 'description')),
            'has_next': notices.has_next(),
            'has_previous': notices.has_previous(),
            'next_page_number': notices.next_page_number() if notices.has_next() else None,
            'previous_page_number': notices.previous_page_number() if notices.has_previous() else None
            }
        return JsonResponse(data)

    return render(request, 'front/pages/notice.html', {'all_notices': notices})