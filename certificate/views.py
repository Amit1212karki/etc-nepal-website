from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from contract.models import *
from batch.models import *
from trainee.models import *
from trainer.models import *
from certificate.models import *
from signatory.models import *
from sponsor.models import *
from django.db.models import Count
from django.db.models.functions import TruncMonth
import json
from signatory.models import Signatory
from django.conf import settings
import os
from django.http import JsonResponse
from django.views.decorators.http import require_GET


# Create your views here.

def loginPage(request):
    return render(request, 'certificate/login.html')

def loginView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=name, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'Welcome back, {request.user.username}! You\'ve successfully logged in.')
                return redirect('/certificate/dashboard/')
            else:
                messages.error(request,'Provided credintial is invalid !!')
                return render(request, 'certificate/login.html')
        except Exception:
            messages.error(request, 'An error occurred !!')
    return render(request, 'certificate/login.html')

@login_required
def home(request):
    data_list = [
    {'label': 'Total Contract', 'value': Contract.objects.count(), 'route':'/contract/'},
    {'label': 'Total Batch', 'value': Batch.objects.count(), 'route': '/batch/'},
    {'label': 'Total Trainer', 'value': Trainer.objects.count(), 'route': '/trainer/'},
    {'label': 'Total Trainee', 'value': Trainee.objects.count(), 'route': '/trainee/'},
    ]

    home_total_trainee_by_month = Trainee.objects.annotate(month=TruncMonth('created_at')).values('month').annotate(count=Count('id')).order_by('month')
    home_selected_trainee_by_month = Trainee.objects.filter(is_selected=True).annotate(month=TruncMonth('created_at')).values('month').annotate(count=Count('id')).order_by('month')
    batch_data = Trainee.objects.values('batch__name').annotate(trainee_count=Count('id')).order_by('batch__name')
    labels = [item['batch__name'] for item in batch_data]
    values = [item['trainee_count'] for item in batch_data]

    total_trainee_data = [

        {
            'month': data['month'].strftime('%b'),
            'total_trainees': data['count']
        }
        for data in home_total_trainee_by_month
    ]
 
    selected_trainee_data = [
        {
            'month': data['month'].strftime('%b'),
            'selected_trainees': data['count']
        }
        for data in home_selected_trainee_by_month
    ]
    context = {
        'data_list':data_list,
        'total_trainee_data': json.dumps(total_trainee_data),  
        'selected_trainee_data': json.dumps(selected_trainee_data),  
        'labels':labels,
        'values':values,
    }
    
    return render(request, 'certificate/home.html', context)

@login_required
def logoutUser(request, id):
    if request.user.is_authenticated and request.user.id == id:
        logout(request)
        messages.success(request, "You have been logged out !!")
        return redirect('/certificate/')
    else:
        messages.error(request, "User can't logout.")
        return redirect('/certificate/dashboard/')
    


@login_required
def certificatIndex(request):
    certificate_trainee = Trainee.objects.filter(is_selected=True)

    context = {
        'certificate_trainee':certificate_trainee,
    }
    return render(request, 'pdfs/certificate/home.html', context)

def generteCertificate1(request, id):
    generate_certificate = get_object_or_404(Trainee, id=id)
    signature = Signatory.objects.all()

    if request.method == 'POST':
        certificates_dir = os.path.join(settings.MEDIA_ROOT, 'certificates')
        sponsor_images_dir = os.path.join(settings.MEDIA_ROOT, 'sponsor_images')

        if not os.path.exists(certificates_dir):
            os.makedirs(certificates_dir)

        if not os.path.exists(sponsor_images_dir):
            os.makedirs(sponsor_images_dir)
        title = request.POST.get('title')
        certificate_number = request.POST.get('certificate_number')
        ctevt_account_number = request.POST.get('ctevt_account_number')
        pan_number = request.POST.get('pan_number')
        sponsor = request.POST.get('sponsor')
        course = request.POST.get('course')
        creditHr = request.POST.get('creditHr')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        municipality = generate_certificate.palika  # Assuming palika is the municipality
        ward_no = generate_certificate.ward_no
        city = generate_certificate.district  # Assuming district can represent the city
        parents_name = f"{generate_certificate.father_name} & {generate_certificate.mother_name}"
        trainee_name = generate_certificate.name
        gender = generate_certificate.gender
        certified_date = date.today()
        certified_date = request.POST.get('certified_date')
        signatory_ids = request.POST.getlist('signatory[]')

        # Handle file uploads if necessary
        image = generate_certificate.image
        sponsor_image1 = request.FILES.get('sponsor_image1')
        sponsor_image2 = request.FILES.get('sponsor_image2')
        sponsor_image3 = request.FILES.get('sponsor_image3')

        sponsor_image_paths = []

        for sponsor_image in [sponsor_image1, sponsor_image2, sponsor_image3]:
            if sponsor_image:
                sponsor_image_path = os.path.join('sponsor_images', sponsor_image.name)  # Create path for each sponsor image
                with open(os.path.join(settings.MEDIA_ROOT, sponsor_image_path), 'wb+') as destination:
                    for chunk in sponsor_image.chunks():
                        destination.write(chunk)
                sponsor_image_paths.append(sponsor_image_path)


        context = {
            'title': title,
            'certificate_number': certificate_number,
            'ctevt_account_number': ctevt_account_number,
            'pan_number': pan_number,
            'sponsor': sponsor,
            'course': course,
            'creditHr': creditHr,
            'start_date': start_date,
            'end_date': end_date,
            'municipality': municipality,
            'ward_no': ward_no,
            'city': city,
            'parents_name': parents_name,
            'trainee_name': trainee_name,
            'certified_date': certified_date,
            'gender': gender,  
            'signatories': Signatory.objects.filter(id__in=signatory_ids),
            'image': f"{settings.MEDIA_URL}{generate_certificate.image}" if generate_certificate.image else None,
            'sponsor_image1': f"{settings.MEDIA_URL}{sponsor_image_paths[0]}" if len(sponsor_image_paths) > 0 else None,
            'sponsor_image2': f"{settings.MEDIA_URL}{sponsor_image_paths[1]}" if len(sponsor_image_paths) > 1 else None,
            'sponsor_image3': f"{settings.MEDIA_URL}{sponsor_image_paths[2]}" if len(sponsor_image_paths) > 2 else None,
            
        }

        # Render the certificate template with the form data
        return render(request, 'pdfs/certificate/certificate_two.html', context)

    context = {
        'generate_certificate': generate_certificate,
        'all_signatory': signature,
    }

    return render(request, 'certificate/certificate/certificate-form2.html', context)



@login_required
def generate(request):
    return render(request, 'pdfs/certificate_safe.html')



def certificateForm(request):
    return render(request, "certificate/certificate/certificate-form.html")

def certificateForm2(request):
    all_signatory = Signatory.objects.all()
    context = {
    "all_signatory": all_signatory
    }
    return render(request, "certificate/certificate/certificate-form2.html", context)
    

def certificateFormGenerate(request):
    # Retrieve all contracts
    certificate_contract = Contract.objects.all()
    certificate_sponsor = Sponsor.objects.all()
    certificate_signature = Signatory.objects.all()

    context = {
        'certificate_contract': certificate_contract,  # Pass the list of contracts and their batches
        'certificate_sponsor': certificate_sponsor,
        'certificate_signature': certificate_signature,
    }

    return render(request, 'certificate/certificate/form.html', context)

def get_batch_from_contract(request, id):
    try:
        contract = Contract.objects.get(pk=id)
        # Get batches associated with the contract
        batches = Batch.objects.filter(contract=contract).values('id', 'name', 'duration', 'start_date', 'end_date', 'seats')  # Adjust fields as necessary

        # Convert the queryset to a list and return as JSON
        return JsonResponse(list(batches), safe=False)
    except Contract.DoesNotExist:
        return JsonResponse({'error': 'Contract not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_student_from_batch(request, id):
    try:
        batch = Batch.objects.get(pk=id)
        # Get batches associated with the contract
        students = Trainee.objects.filter(batch=batch,is_selected=True).values('id','name','image')

        # Convert the queryset to a list and return as JSON
        return JsonResponse(list(students), safe=False)
    except Contract.DoesNotExist:
        return JsonResponse({'error': 'Students not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@require_GET
def generate_certificate(request):
    # Extract parameters from the request
    student_id = request.GET.get('student_id')
    contract_id = request.GET.get('contract_id')
    batch_id = request.GET.get('batch_id')
    certificate_format = request.GET.get('certificate_format')
    selected_signatories = json.loads(request.GET.get('selected_signatories', '[]'))  # Parse JSON
    selected_sponsors = json.loads(request.GET.get('selected_sponsors', '[]'))  # Parse JSON

    # Fetch the related objects
    student = Trainee.objects.get(pk=student_id)
    contract = Contract.objects.get(pk=contract_id)
    batch = Batch.objects.get(pk=batch_id)

    # Fetch signatories
    signatories = [Signatory.objects.get(pk=data) for data in selected_signatories]

    # Fetch sponsors
    sponsors = [Sponsor.objects.get(pk=data) for data in selected_sponsors]

    context = {
        "student": {
            "name": student.name,
            "nepali_name": student.nepali_name,
            "image": student.image,
            "gender": student.get_gender_display(),
            "date_of_birth_ad": student.date_of_birth_ad,
            "date_of_birth_bs": student.date_of_birth_bs,
            "age": student.age,
            "marital_status": student.get_marital_status_display(),
            "ethnic_group": student.ethnic_group,
            "mother_name": student.mother_name,
            "father_name": student.father_name,
            "nepali_father_name":student.nepali_father_name,
            "citizenship_no": student.citizenship_no,
            "issue_date": student.issue_date,
            "issue_district": student.issue_district,
            "phone_no": student.phone_no,
            "email": student.email,
            "qualification": student.qualification,
            "province": student.province.name if student.province else None,
            "district": student.district.name if student.district else None,
            "nepali_district": student.district.nepali_name if student.district else None,
            "palika": student.palika.name if student.palika else None,
            "nepali_palika_name": student.palika.nepali_name if student.palika else None,
            "ward_no": student.ward_no,
            "occupation": student.occupation,
            'qr_code': student.qr_code_image.url if student.qr_code_image else None, 

        },
        "contract": {
            "id": contract.id,
            "name": contract.name,
            "nepali_name": contract.nepali_name,
            "location": contract.location,
            "nepali_location": contract.nepali_location,
            "occupation": contract.occupation,
            "nepali_occupation": contract.nepali_occupation,
            "donation_by": contract.donation_by,
            "nepali_donation_by": contract.nepali_donation_by,

        },
        "batch": {
            "id": batch.id,
            "name": batch.name,
            "duration": batch.duration,
            "start_date": batch.start_date,
            "end_date": batch.end_date,
            "seats": batch.seats,
            "trainers": [
                {
                    "id": trainer.id,
                    "name": trainer.name,
                    "nepali_name": trainer.nepali_name,
                } for trainer in batch.trainer.all()
            ],
        },
        "signatories": [
            {
                "id": signatory.id,
                "name": signatory.name,
                "nepali_name": signatory.nepali_name,
                "designation": signatory.designation,
                "nepali_designation": signatory.nepali_designation,
                "institution": signatory.institution,
                "nepali_institution": signatory.nepali_institution,

            } for signatory in signatories
        ],
        "sponsors": [
            {
                "id": sponsor.id,
                "name": sponsor.name,
                "nepali_name": sponsor.nepali_name,
                "logo": sponsor.image.url if sponsor.image else None,
            } for sponsor in sponsors
        ],
        "municipality_name": request.GET.get('municipality_name'),
        "municipality_second_name": request.GET.get('municipality_second_name'),
        "municipality_address": request.GET.get('municipality_address'),
        "vocational_first_heading": request.GET.get('vocational_first_heading'),
        "vocational_second_heading": request.GET.get('vocational_second_heading'),
        "vocational_third_heading": request.GET.get('vocational_third_heading'),
        "vocational_fourth_heading": request.GET.get('vocational_fourth_heading'),
        
    }

    # Render the appropriate template based on the certificate format
    if certificate_format == 'etc certificate':
        return render(request, 'pdfs/certificate/college_certificate.html', context)
    elif certificate_format == 'municipality certificate':
        return render(request, 'pdfs/certificate/municipality_certificate.html', context)
    else:
        return render(request, 'pdfs/certificate/vocational_certificate.html', context)



def trainee_details(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    return render(request, 'certificate/detail.html', {'trainee': trainee})
