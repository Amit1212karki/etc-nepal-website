from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from contract.models import *
from batch.models import *
from location.models import *
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

@csrf_exempt  # Use with caution; for production, ensure you handle CSRF properly
def toggle_selection(request, trainee_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        is_selected = data.get('is_selected')

        try:
            trainee = Trainee.objects.get(id=trainee_id)
            trainee.is_selected = is_selected
            trainee.save()
            return JsonResponse({'status': 'success', 'is_selected': is_selected})
        except Trainee.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Trainee not found.'}, status=404)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'}, status=405)

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
        contract_id = request.POST.get('contract')
        batch_id = request.POST.get('batch')
        province_id = request.POST.get('province')
        district_id = request.POST.get('district')
        palika_id = request.POST.get('palika')
        ward_no  =  request.POST.get('ward_no')
        occupation = request.POST.get('occupation')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        date_of_birth_ad = request.POST.get('dob')
        date_of_birth_bs = request.POST.get('dob_bs')
        

        age  =  request.POST.get('age')
        if age:
            age  =  int(age)
        else:
            age  =  0
        marital_status = request.POST.get('marital_status')
        ethnic_group = request.POST.get('ethnic_group')
        mother_name = request.POST.get('mother_name')
        father_name = request.POST.get('father_name')
        citizenship_no = request.POST.get('citizenship_no')
        issue_date = request.POST.get('issue_date')
        issue_district = request.POST.get('issue_district')
        phone_no = request.POST.get('contact')
        email = request.POST.get('email')
        qualification = request.POST.get('qualification')
        image = request.FILES.get('image')
        citizenship_front_image = request.FILES.get('citizenship_front_image')
        citizenship_back_image = request.FILES.get('citizenship_back_image')
        is_selected = request.POST.get('is_selected')

        
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
            ward_no=ward_no,
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
    edit_trainee = get_object_or_404(Trainee, id=id)
    edit_trainee_contract = Contract.objects.all()
    edit_trainee_batch = Batch.objects.all()
    edit_trainee_province = Province.objects.all()
    edit_trainee_district = District.objects.all()
    edit_trainee_palika = Palika.objects.all()
    context = {
        'trainee':edit_trainee,
        'trainee_batch':edit_trainee_batch,
        'trainee_contract':edit_trainee_contract,
        'trainee_province':edit_trainee_province,
        'trainee_district':edit_trainee_district,
        'trainee_palika':edit_trainee_palika
    }
    return render(request, 'certificate/trainee/edit.html', context)


def traineeUpdate(request, id):
    update_trainee = get_object_or_404(Trainee, id=id)
    if request.method == "POST":
        contract_id = request.POST.get('contract')
        batch_id = request.POST.get('batch')
        province_id = request.POST.get('province')
        district_id = request.POST.get('district')
        palika_id = request.POST.get('palika')
        ward_no  =  request.POST.get('ward_no')
        occupation = request.POST.get('occupation')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        date_of_birth_ad = request.POST.get('dob')
        date_of_birth_bs = request.POST.get('dob_bs')
        

        age  =  request.POST.get('age')
        if age:
            age  =  int(age)
        else:
            age  =  0
        marital_status = request.POST.get('marital_status')
        ethnic_group = request.POST.get('ethnic_group')
        mother_name = request.POST.get('mother_name')
        father_name = request.POST.get('father_name')
        citizenship_no = request.POST.get('citizenship_no')
        issue_date = request.POST.get('issue_date')
        issue_district = request.POST.get('issue_district')
        phone_no = request.POST.get('contact')
        email = request.POST.get('email')
        qualification = request.POST.get('qualification')
        image = request.FILES.get('image') or update_trainee.image
        citizenship_front_image = request.FILES.get('citizenship_front_image') or update_trainee.citizenship_front_image
        citizenship_back_image = request.FILES.get('citizenship_back_image') or update_trainee.citizenship_back_image

        is_selected = request.POST.get('is_selected')

        contract = get_object_or_404(Contract, id=contract_id)
        batch = get_object_or_404(Batch, id=batch_id)
        province = get_object_or_404(Province, id=province_id)
        district = get_object_or_404(District, id=district_id)
        palika = get_object_or_404(Palika, id=palika_id)

        update_trainee.contract = contract
        update_trainee.batch = batch
        update_trainee.province = province
        update_trainee.district = district
        update_trainee.palika = palika
        update_trainee.ward_no=ward_no
        update_trainee.occupation = occupation
        update_trainee.name = name
        update_trainee.gender = gender
        update_trainee.date_of_birth_ad=date_of_birth_ad
        update_trainee.date_of_birth_bs=date_of_birth_bs
        update_trainee.age=age
        update_trainee.marital_status=marital_status
        update_trainee.ethnic_group=ethnic_group
        update_trainee.mother_name=mother_name
        update_trainee.father_name=father_name
        update_trainee.citizenship_no=citizenship_no
        update_trainee.issue_date=issue_date
        update_trainee.issue_district=issue_district
        update_trainee.phone_no=phone_no
        update_trainee.email=email
        update_trainee.qualification=qualification
        update_trainee.image=image
        update_trainee.citizenship_front_image=citizenship_front_image
        update_trainee.citizenship_back_image=citizenship_back_image
        update_trainee.is_selected= (is_selected == 'yes')

        update_trainee.save()
        messages.success(request, 'Trainee successfully updated.')
        return redirect('trainee-index')
    else:
        messages.error(request, 'Error while updating the trainee !!')
        return redirect(request, 'certificate/trainee/edit.html')
    

def traineeDelete(request, id):
    try:
        delete_trainee = get_object_or_404(Trainee, id=id)
        delete_trainee.delete()
        messages.success(request, 'Trainee successfully Deleted.')
        return redirect('trainee-index')
    except:
        messages.error(request, 'Trainee not found. Deletion failed !!')
    return redirect('trainee-index')