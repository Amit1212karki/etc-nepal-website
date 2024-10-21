from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Signatory
from django.contrib import messages

# Create your views here.

@login_required
def signatoryIndex(request):
    all_signatories = Signatory.objects.all()

    context = {
        'all_signatories': all_signatories
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
