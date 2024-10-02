from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Trainee  # Ensure Trainee model is imported
from batch.models import *
from contract.models import *

# Create your views here.

@login_required
def traineeIndex(request):
    """View to list all trainees."""
    all_trainees = Trainee.objects.all()
    context = {
        'all_trainees': all_trainees
    }
    return render(request, 'certificate/trainee/index.html', context)

@login_required
def traineeCreate(request):
    """View to show the trainee creation form."""
    batch_all = Batch.objects.all()
    contract_all = Contract.objects.all()
    context = {
        "batch_all" : batch_all,
        "contract_all" : contract_all
    }
    return render(request, 'certificate/trainee/add.html', context)

@login_required
def traineeStore(request):
    """View to handle the storage of a new trainee."""
    if request.method == 'POST':
        contract = request.POST.get('contract')
        batch = request.POST.get('batch')
        province = request.POST.get('province')
        district = request.POST.get('district')
        palika = request.POST.get('palika')
        occupation = request.POST.get('occupation')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        date_of_birth_ad = request.POST.get('date_of_birth_ad')
        date_of_birth_bs = request.POST.get('date_of_birth_bs')
        marital_status = request.POST.get('marital_status')
        ethnic_group = request.POST.get('ethnic_group')
        mother_name = request.POST.get('mother_name')
        father_name = request.POST.get('father_name')
        citizenship_no = request.POST.get('citizenship_no')
        issue_date = request.POST.get('issue_date')
        issue_district = request.POST.get('issue_district')
        phone_no = request.POST.get('phone_no')
        email = request.POST.get('email')
        qualification = request.POST.get('qualification')
        image = request.FILES.get('image')
        citizenship_front_image = request.FILES.get('citizenship_front_image')
        citizenship_back_image = request.FILES.get('citizenship_back_image')

        # Create the Trainee object
        trainee = Trainee.objects.create(
            contract_id=contract,
            batch_id=batch,
            province_id=province,
            district_id=district,
            palika_id=palika,
            occupation=occupation,
            name=name,
            gender=gender,
            date_of_birth_ad=date_of_birth_ad,
            date_of_birth_bs=date_of_birth_bs,
            marital_status=marital_status,
            ethnic_group=ethnic_group,
            mother_name=mother_name,
            father_name=father_name,
            citizenship_no=citizenship_no,
            issue_date=issue_date,
            issue_district=issue_district,
            phone_no=phone_no,
            email=email,
            qualification=qualification,
            image=image,
            citizenship_front_image=citizenship_front_image,
            citizenship_back_image=citizenship_back_image,
            is_selected=False  # Default value
        )
        messages.success(request, 'Trainee successfully created.')
        return redirect('trainee-index')

    messages.error(request, 'All fields are required!!')
    return render(request, 'certificate/trainee/add.html')

@login_required
def traineeEdit(request, id):
    """View to show the form for editing a trainee."""
    edit_trainee = get_object_or_404(Trainee, id=id)

    context = {
        'edit_trainee': edit_trainee,
    }
    return render(request, 'certificate/trainee/edit.html', context)

@login_required
def traineeUpdate(request, id):
    """View to handle the updating of a trainee's details."""
    update_trainee = get_object_or_404(Trainee, id=id)
    if request.method == 'POST':
        update_trainee.contract_id = request.POST.get('contract')
        update_trainee.batch_id = request.POST.get('batch')
        update_trainee.province_id = request.POST.get('province')
        update_trainee.district_id = request.POST.get('district')
        update_trainee.palika_id = request.POST.get('palika')
        update_trainee.occupation = request.POST.get('occupation')
        update_trainee.name = request.POST.get('name')
        update_trainee.gender = request.POST.get('gender')
        update_trainee.date_of_birth_ad = request.POST.get('date_of_birth_ad')
        update_trainee.date_of_birth_bs = request.POST.get('date_of_birth_bs')
        update_trainee.marital_status = request.POST.get('marital_status')
        update_trainee.ethnic_group = request.POST.get('ethnic_group')
        update_trainee.mother_name = request.POST.get('mother_name')
        update_trainee.father_name = request.POST.get('father_name')
        update_trainee.citizenship_no = request.POST.get('citizenship_no')
        update_trainee.issue_date = request.POST.get('issue_date')
        update_trainee.issue_district = request.POST.get('issue_district')
        update_trainee.phone_no = request.POST.get('phone_no')
        update_trainee.email = request.POST.get('email')
        update_trainee.qualification = request.POST.get('qualification')
        
        # Check if images are uploaded
        if 'image' in request.FILES:
            update_trainee.image = request.FILES['image']
        if 'citizenship_front_image' in request.FILES:
            update_trainee.citizenship_front_image = request.FILES['citizenship_front_image']
        if 'citizenship_back_image' in request.FILES:
            update_trainee.citizenship_back_image = request.FILES['citizenship_back_image']

        update_trainee.save()
        messages.success(request, 'Trainee successfully updated.')
        return redirect('trainee-index')

    return render(request, 'certificate/trainee/edit.html', {'edit_trainee': update_trainee})

@login_required
def traineeDelete(request, id):
    """View to handle the deletion of a trainee."""
    delete_trainee = get_object_or_404(Trainee, id=id)
    delete_trainee.delete()
    messages.success(request, 'Trainee successfully deleted.')
    return redirect('trainee-index')
