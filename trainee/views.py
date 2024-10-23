from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from contract.models import *
from batch.models import *
from location.models import *
from .models import *
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
import qrcode
import json
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from io import BytesIO
from django.conf import settings
from datetime import datetime
from dateutil import parser
from django.urls import reverse



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
    search_query = request.GET.get('search','')
    all_trainee = Trainee.objects.filter(
        Q(name__icontains=search_query)
    ) if search_query else Trainee.objects.all()

    paginator = Paginator(all_trainee, 7)
    page_number = request.GET.get('page', 1)
    trainee = paginator.get_page(page_number)

    total_entries = paginator.count
    total_pages = paginator.num_pages
    start_index = trainee.start_index()
    end_index = trainee.end_index()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'trainee': [
                {
                    'id': trainee.id,
                    'name': trainee.name,
                    'image': trainee.image.url if trainee.image else None,
                    'qr_code': trainee.qr_code_image.url if trainee.qr_code_image else None,

                    'contract': {
                        'id': trainee.contract.id,  # or use t.contract.name if you have a name field
                        'name': trainee.contract.name  # assuming Contract model has a name field
                    },
                    'batch': {
                        'id': trainee.batch.id,  # similarly for Batch, extract relevant fields
                        'name': trainee.batch.name
                    },
                    'phone_no': trainee.phone_no,
                    'is_selected':trainee.is_selected,
                }
                for trainee in trainee.object_list
            ],
            'has_next': trainee.has_next(),
            'has_previous': trainee.has_previous(),
            'next_page_number': trainee.next_page_number() if trainee.has_next() else None,
            'previous_page_number': trainee.previous_page_number() if trainee.has_previous() else None,
            'total_entries': total_entries,
            'total_pages': total_pages,
            'current_page': trainee.number,
            'start_index': start_index,
            'end_index': end_index,
        }

        return JsonResponse(data)

    context = {
        'all_trainee':all_trainee
    }

    return render(request, 'certificate/trainee/index.html',context)



@login_required
def traineeCreate(request):
    trainee_contract = Contract.objects.all()
    trainee_batch = Batch.objects.filter(seats__gte=1)
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
        nepali_name = request.POST.get('nepali_name')
        gender = request.POST.get('gender')
        date_of_birth_ad = request.POST.get('dob')
        date_of_birth_bs = request.POST.get('dob_bs')
        try:
            if date_of_birth_bs:
                parsed_date_bs = parser.parse(date_of_birth_bs)
                date_of_birth_bs = parsed_date_bs.strftime('%Y-%m-%d')
        except (ValueError, parser.ParserError):
            messages.error(request, 'Invalid BS date format. Please enter a valid date.')
            return redirect('trainee-create')
        

        age  =  request.POST.get('age')
        if age:
            age  =  int(age)
        else:
            age  =  0
        marital_status = request.POST.get('marital_status')
        ethnic_group = request.POST.get('ethnic_group')
        mother_name = request.POST.get('mother_name')
        father_name = request.POST.get('father_name')
        nepali_father_name = request.POST.get('nepali_father_name')
        citizenship_no = request.POST.get('citizenship_no')
        issue_date = request.POST.get('issue_date')
        try:
            if issue_date:
                parsed_issue_date = parser.parse(issue_date)
                issue_date = parsed_issue_date.strftime('%Y-%m-%d')
        except (ValueError, parser.ParserError):
            messages.error(request, 'Invalid issue date format. Please enter a valid date.')
            return redirect('trainee-create')
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
        if batch.seats <= 0:
            messages.error(request, 'No available seats in this batch. Please select a different batch.')
            return redirect('trainee-create')
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
            nepali_name = nepali_name,
            gender = gender,
            date_of_birth_ad=date_of_birth_ad,
            date_of_birth_bs=date_of_birth_bs,
            age=age,
            marital_status=marital_status,
            ethnic_group=ethnic_group,
            mother_name=mother_name,
            father_name=father_name,
            nepali_father_name = nepali_father_name,
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
        trainee_detail_url = request.build_absolute_uri(reverse('certificate-scan', kwargs={'id': store_trainee.id}))


        qr_data = {
            "url": request.build_absolute_uri(trainee_detail_url),
            "name": name,
            "nepali_name": nepali_name,
            "gender": gender,
            "date_of_birth_ad": date_of_birth_ad,
            "age": age,
            "contact": phone_no,
            "email": email,
            "occupation": occupation,
            "contract": contract.name,
            "batch": batch.name,
            "province": province.name,
            "district": district.name,
            "palika": palika.name,
            "ward_no": ward_no,
        }

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(json.dumps(qr_data))
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')

        # Save QR code to a BytesIO object
        qr_io = BytesIO()
        img.save(qr_io, 'PNG')
        qr_io.seek(0)

        # Save the QR code image in the media folder
        qr_code_filename = f'trainee/qr_code_images/{store_trainee.id}_qr.png'
        default_storage.save(qr_code_filename, ContentFile(qr_io.read()))

        # Update the Trainee object with the QR code path
        store_trainee.qr_code_image = qr_code_filename  # save the relative path
        store_trainee.save()

        batch.seats -=1
        batch.save()
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
        nepali_name = request.POST.get('nepali_name')
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
        nepali_father_name = request.POST.get('nepali_father_name')
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
        update_trainee.nepali_name = nepali_name
        update_trainee.gender = gender
        update_trainee.date_of_birth_ad=date_of_birth_ad
        update_trainee.date_of_birth_bs=date_of_birth_bs
        update_trainee.age=age
        update_trainee.marital_status=marital_status
        update_trainee.ethnic_group=ethnic_group
        update_trainee.mother_name=mother_name
        update_trainee.father_name=father_name
        update_trainee.nepali_father_name = nepali_father_name
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