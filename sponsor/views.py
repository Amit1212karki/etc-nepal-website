from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def sponsorIndex(request):
    all_sponsor = Sponsor.objects.all()
    context = {
        'all_sponsor':all_sponsor
    }
    return render(request, 'certificate/sponsor/index.html', context)

@login_required
def sponsorAdd(request):
    return render(request, 'certificate/sponsor/add.html')

@login_required
def sponsorStore(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        if name and image:
            sponsor = Sponsor.objects.create(
                name = name,
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
