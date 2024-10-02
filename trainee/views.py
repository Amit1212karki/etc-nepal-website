from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from contract.models import *
from batch.models import *
from location.models import *
from .models import *
from django.contrib import messages


# Create your views here.

@login_required
def traineeIndex(request):
    all_trainee = Trainee.objects.all()
    context = {
        'all_trainee':all_trainee
    }

    return render(request, 'certificate/trainee/index.html',context)

@login_required
def traineeCreate(request):
    trainee_contract = Contract.objects.all()
    trainee_batch = Batch.objects.all()
    trainee_province = Province.objects.all()
    trainee_district = District.objects.all()
    trainee_palika = Palika.objects.all()

    context = {
        'trainee_contract':trainee_contract,
        'trainee_batch':trainee_batch,
        'trainee_province':trainee_province,
        'trainee_district':trainee_district,
        'trainee_palika':trainee_palika
    }
    return render(request, 'certificate/trainee/add.html', context)


@login_required
def traineeStore(request):
    if request.method == 'POST':
        print(request.POST)
        contract_id=request.POST.get('contract')
        batch_id=request.POST.get('batch')
        province_id=request.POST.get('province')
        district_id=request.POST.get('district')
        palika_id=request.POST.get('palika')
        occupation=request.POST.get('occupation')
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        date_of_birth_ad=request.POST.get('dob')
        date_of_birth_bs=request.POST.get('dob_bs')
        

        age = request.POST.get('age')
        if age:
            age = int(age)
        else:
            age = 0
        marital_status=request.POST.get('marital_status')
        ethnic_group=request.POST.get('ethnic_group')
        mother_name=request.POST.get('mother_name')
        father_name=request.POST.get('father_name')
        citizenship_no=request.POST.get('citizenship_no')
        issue_date=request.POST.get('issue_date')
        issue_district=request.POST.get('issue_district')
        phone_no=request.POST.get('contact')
        email=request.POST.get('email')
        qualification=request.POST.get('qualification')
        image=request.FILES.get('image')
        citizenship_front_image=request.FILES.get('citizenship_front_image')
        citizenship_back_image=request.FILES.get('citizenship_back_image')
        is_selected=request.POST.get('is_selected')

        
        contract = get_object_or_404(Contract, id=contract_id)
        batch = get_object_or_404(Batch, id=batch_id)
        province = get_object_or_404(Province, id=province_id)
        district = get_object_or_404(District, id=district_id)
        palika = get_object_or_404(Palika, id=palika_id)

        store_trainee = Trainee.objects.create(
            contract = contract,
            batch = batch,
            province = province,
            district = district,
            palika = palika,
            occupation = occupation,
            name = name,
            gender = gender,
            date_of_birth_ad=date_of_birth_ad,
            date_of_birth_bs=date_of_birth_bs,
            age=age,
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
            is_selected= (is_selected == 'yes')
        )
        store_trainee.save()
        messages.success(request, 'Trainee added successfully')
        return redirect('trainee-index')
    else:
        messages.error(request,'Something went wrong!!')
    return render(request, 'certificate/trainee/add.html')


@login_required
def traineeEdit(request, id):
    return render(request, 'certificate/trainee/edit.html')