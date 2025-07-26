from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import JsonResponse
# Create your views here.

@login_required
def trainerIndex(request):
    search_query = request.GET.get('search', '')
    all_trainer = Trainer.objects.filter(
        Q(name__icontains=search_query) | Q(qualification__icontains=search_query)
    ) if search_query else Trainer.objects.all()

    paginator = Paginator(all_trainer, 7)
    page_number = request.GET.get('page', 1)
    trainer = paginator.get_page(page_number)

    total_entries = paginator.count
    total_pages = paginator.num_pages 
    start_index = trainer.start_index()
    end_index = trainer.end_index()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'trainer': list(trainer.object_list.values('id', 'name', 'contact', 'qualification', 'tot')),
            'has_next': trainer.has_next(),
            'has_previous': trainer.has_previous(),
            'next_page_number': trainer.next_page_number() if trainer.has_next() else None,
            'previous_page_number': trainer.previous_page_number() if trainer.has_previous() else None,
            'total_entries': total_entries,
            'total_page': paginator.num_pages,
            'total_pages': total_pages,
            'current_page': trainer.number,
            'start_index': start_index,
            'end_index': end_index
        }
        return JsonResponse(data)

    context = {
        'all_trainer': trainer
    }
    return render(request, 'certificate/trainer/index.html', context)

@login_required
def trainerCreate(request):
    return render(request, 'certificate/trainer/add.html')

@login_required
def trainerStore(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        nepali_name = request.POST.get('nepali_name')
        contact = request.POST.get('contact')
        qualification = request.POST.get('qualification')
        tot = request.POST.get('tot')

        trainer = Trainer.objects.create(
            name = name,
            contact = contact,
            nepali_name = nepali_name,
            qualification = qualification,
            tot=(tot == 'yes')
        )
        trainer.save()
        messages.success(request, 'Trainer successfully created.')
        return redirect('trainer-index')
    else:
        messages.error(request,'All fields are required!!')
    return render(request, 'certificate/trainer/add.html')

@login_required
def trainerEdit(request, id):
    edit_trainer = get_object_or_404(Trainer, id=id)

    context = {
        'edit_trainer':edit_trainer,
    }
    return render(request, 'certificate/trainer/edit.html', context)


@login_required
def trainerUpdate(request, id):
    update_trainer = Trainer.objects.get(id=id)
    if request.method == 'POST':
        update_trainer.name = request.POST.get('name')
        update_trainer.nepali_name = request.POST.get('nepali_name')
        update_trainer.contact = request.POST.get('contact')
        update_trainer.qualification = request.POST.get('qualification')
        tot = request.POST.get('tot', 'no')  # Default to 'no'
        update_trainer.tot = True if tot == 'yes' else False

        if update_trainer.name and update_trainer.nepali_name and update_trainer.contact and update_trainer.qualification:
            update_trainer.save()
            messages.success(request,'Trainer successfully updated.')
            return redirect('trainer-index')
        else:
            messages.error(request, 'All fields are required!')
            return render(request, 'certificate/trainer/edit.html')
    return render(request, 'certificate/trainer/edit.html')


def trainerDelete(request, id):
    try:
        delete_trainer = Trainer.objects.get(id=id)
        delete_trainer.delete()
        messages.success(request, 'Trainer successfully Deleted.')
        return redirect('trainer-index')
    except:
        messages.error(request, 'Trainer not found. Deletion failed !!')
    return redirect('trainer-index')

