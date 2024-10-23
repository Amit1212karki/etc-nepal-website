from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.

@login_required
def sponsorIndex(request):
    search_query = request.GET.get('search','')
    all_sponsor = Sponsor.objects.filter(
        Q(name__icontains=search_query)
    ) if search_query else Sponsor.objects.all()

    paginator = Paginator(all_sponsor, 7)
    page_number = request.GET.get('page', 1)
    sponsors = paginator.get_page(page_number)

    total_entries = paginator.count
    total_pages = paginator.num_pages
    start_index = sponsors.start_index()
    end_index = sponsors.end_index()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'sponsors': [
                {
                    'id': sponsor.id,
                    'name': sponsor.name,
                    'image': sponsor.image.url if sponsor.image else None
                }
                for sponsor in sponsors.object_list
            ],
            'has_next': sponsors.has_next(),
            'has_previous': sponsors.has_previous(),
            'next_page_number': sponsors.next_page_number() if sponsors.has_next() else None,
            'previous_page_number': sponsors.previous_page_number() if sponsors.has_previous() else None,
            'total_entries': total_entries,
            'total_pages': total_pages,
            'current_page': sponsors.number,
            'start_index': start_index,
            'end_index': end_index,
        }

        return JsonResponse(data)

    context = {
        'all_sponsor':sponsors
    }
    return render(request, 'certificate/sponsor/index.html', context)

@login_required
def sponsorAdd(request):
    return render(request, 'certificate/sponsor/add.html')

@login_required
def sponsorStore(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        nepali_name = request.POST.get('nepali_name')
        image = request.FILES.get('image')
        if name and image:
            sponsor = Sponsor.objects.create(
                name = name,
                nepali_name = nepali_name,
                image = image
            )
            sponsor.save()
            messages.success(request, 'Sponsor successfully created.')
            return redirect('sponsor-index')
        else:
            messages.error(request, 'All fields are required!')
    return render(request, 'certificate/sponsor/add.html')


def sponsorEdit(request, id):
    edit_sponsor = get_object_or_404(Sponsor, id=id)
    context = {
        'edit_sponsor': edit_sponsor,
    }
    return render(request, 'certificate/sponsor/edit.html', context)

def sponsorUpdate(request,id):
    update_sponsor = Sponsor.objects.get(id=id)

    if request.method == "POST":
        update_sponsor.name = request.POST.get('name')
        update_sponsor.nepali_name = request.POST.get('nepali_name')
        if 'image' in request.FILES:
            update_sponsor.image = request.FILES['image']
        if update_sponsor.name:
            update_sponsor.save()
            messages.success(request, 'Sponsor successfully updated.')
            return redirect('sponsor-index')
        else:
            messages.error(request, 'All fields are required!')
            
    else:
        messages.error(request, 'All fields are required!')
        return render(request, 'certificate/sponsor/edit.html')



def sponsorDelete(request,id):
    try:
        delete_sponsor = Sponsor.objects.get(id=id)
        delete_sponsor.delete()
        messages.success(request, 'Sponsor successfully deleted.')
    except:
        messages.error(request, 'Sponsor not found. Deletion failed.')
    return redirect('sponsor-index')
