from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages

# Create your views here.

@login_required
def contractIndex(request):
    all_contract = Contract.objects.all()

    context = {
        'all_contract':all_contract
    }
    return render(request, 'certificate/contract/index.html', context)


@login_required
def contractCreate(request):
    return render(request, 'certificate/contract/add.html')

@login_required
def contractStore(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        location = request.POST.get('location')
        occupation = request.POST.get('occupation')
        donation_by = request.POST.get('donation')

        contract = Contract.objects.create(
            name=name,
            location=location,
            occupation=occupation,
            donation_by=donation_by
        )
        contract.save()
        messages.success(request, 'Contract successfully created.')
        return redirect('contract-index')
    else:
        messages.error(request,'All fields are required!!')    
    return render(request, 'certificate/contract/add.html')


@login_required
def contractEdit(request, id):
    edit_contract = Contract.objects.get(id=id)
    context = {
        'edit_contract':edit_contract
    }
    return render(request, 'certificate/contract/edit.html', context)


@login_required
def contractUpdate(request, id):
    update_contract = get_object_or_404(Contract, id=id)
    if request.method == 'POST':
        update_contract.name = request.POST.get('name')
        update_contract.location = request.POST.get('location')
        update_contract.occupation = request.POST.get('occupation')
        update_contract.donation_by = request.POST.get('donation')

        if update_contract.name and update_contract.location and update_contract.occupation and update_contract.donation_by:
            update_contract.save()
            messages.success(request, 'Contract successfully updated.')
            return redirect('contract-index')
        else:
            messages.error(request, 'All fields are required!')

    return render(request, 'certificate/contract/edit.html')

def contractDelete(request, id):
    try:
        delete_contract = Contract.objects.get(id=id)
        delete_contract.delete()
        messages.success(request, 'Contract successfully Deleted.')
        return redirect('contract-index')
    except:
        messages.error(request, 'Contract not found. Deletion failed !!')
    return redirect('contract-index')
        