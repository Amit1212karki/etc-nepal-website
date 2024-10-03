from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
# Create your views here.

@login_required
def trainerIndex(request):
    all_trainer = Trainer.objects.all()
    context = {
        'all_trainer':all_trainer
    }
    return render(request, 'certificate/trainer/index.html', context)

@login_required
def trainerCreate(request):
    return render(request, 'certificate/trainer/add.html')

@login_required
def trainerStore(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        qualification = request.POST.get('qualification')
        tot = request.POST.get('tot')

        trainer = Trainer.objects.create(
            name = name,
            contact = contact,
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
        update_trainer.contact = request.POST.get('contact')
        update_trainer.qualification = request.POST.get('qualification')
        tot = request.POST.get('tot', 'no')  # Default to 'no'
        update_trainer.tot = True if tot == 'yes' else False

        if update_trainer.name and update_trainer.contact and update_trainer.qualification:
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

