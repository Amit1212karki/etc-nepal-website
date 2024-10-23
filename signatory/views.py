from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Signatory
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.

@login_required
def signatoryIndex(request):
    search_query = request.GET.get('search','')
    all_signatories = Signatory.objects.filter(
        Q(name__icontains=search_query) |  Q(designation__icontains=search_query) |  Q(institution__icontains=search_query)
    ) if search_query else Signatory.objects.all()
    
    paginator = Paginator(all_signatories, 7)
    page_number = request.GET.get('page',1)
    signatories = paginator.get_page(page_number) 
    total_entries = paginator.count
    total_pages = paginator.num_pages
    start_index = signatories.start_index()
    end_index = signatories.end_index()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'signatories':list(signatories.object_list.values('id','name','institution','designation')),
            'has_next': signatories.has_next(),
            'has_previous': signatories.has_previous(),
            'next_page_number': signatories.next_page_number() if signatories.has_next() else None,
            'previous_page_number': signatories.previous_page_number() if signatories.has_previous() else None,
            'total_entries': total_entries,
            'total_page': paginator.num_pages,
            'total_pages': total_pages,
            'current_page': signatories.number,
            'start_index': start_index,
            'end_index': end_index
        }
        return JsonResponse(data)

    context = {
        'all_signatories': signatories
    }
    return render(request, 'certificate/signatory/index.html', context)


@login_required
def signatoryCreate(request):
    return render(request, 'certificate/signatory/add.html')


@login_required
def signatoryStore(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        institution = request.POST.get('institution')
        nepali_name = request.POST.get('nepali_name')  
        nepali_designation = request.POST.get('nepali_designation')  
        nepali_institution = request.POST.get('nepali_institution')  


        if name and designation and institution:
            signatory = Signatory.objects.create(
                name=name,
                designation=designation,
                institution=institution,
                nepali_name = nepali_name,
                nepali_designation = nepali_designation,
                nepali_institution = nepali_institution,
            )
            signatory.save()
            messages.success(request, 'Signatory successfully created.')
            return redirect('signatory-index')
        else:
            messages.error(request, 'All fields are required!')
    return render(request, 'certificate/signatory/add.html')


@login_required
def signatoryEdit(request, id):
    signatory = get_object_or_404(Signatory, id=id)
    context = {
        'signatory': signatory
    }
    return render(request, 'certificate/signatory/edit.html', context)


@login_required
def signatoryUpdate(request, id):
    signatory = get_object_or_404(Signatory, id=id)
    if request.method == 'POST':
        signatory.name = request.POST.get('name')
        signatory.designation = request.POST.get('designation')
        signatory.institution = request.POST.get('institution')

        signatory.nepali_name = request.POST.get('nepali_name')  
        signatory.nepali_designation = request.POST.get('nepali_designation')  
        signatory.nepali_institution = request.POST.get('nepali_institution') 
        
        # Update the image only if a new one is provided
        if 'image' in request.FILES:
            signatory.image = request.FILES['image']

        if signatory.name and signatory.designation and signatory.institution and signatory.nepali_name and signatory.nepali_designation and signatory.nepali_institution :
            signatory.save()
            messages.success(request, 'Signatory successfully updated.')
            return redirect('signatory-index')
        else:
            messages.error(request, 'All fields are required!')

    return render(request, 'certificate/signatory/edit.html', {'signatory': signatory})


@login_required
def signatoryDelete(request, id):
    try:
        signatory = get_object_or_404(Signatory, id=id)
        signatory.delete()
        messages.success(request, 'Signatory successfully deleted.')
    except:
        messages.error(request, 'Signatory not found. Deletion failed.')
    return redirect('signatory-index')
