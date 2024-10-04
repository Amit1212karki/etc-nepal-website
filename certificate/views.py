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
from django.template.loader import get_template
from django.http import HttpResponse
from etcportfolio import renderers
import base64
from datetime import datetime
import mimetypes
from django.db.models import Count
from django.db.models.functions import TruncMonth
import json
from django.template.loader import get_template
from django.http import HttpResponse
from signatory.models import Signatory
from django.conf import settings
import os

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
    {'label': 'Total Certificate', 'value': Certificate.objects.count(), 'route': '/certificate/'},
    {'label': 'Total Signatory', 'value': Signatory.objects.count(), 'route': '/signatory/'},
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
    # all_signatory = 
    # context = {
    # "all_signatory": 
    # }
    return render(request, "certificate/certificate/certificate-form.html")

def certificateForm2(request):
    all_signatory = Signatory.objects.all()
    context = {
    "all_signatory": all_signatory
    }
    return render(request, "certificate/certificate/certificate-form2.html", context)

def pdf_view(request, *args, **kwargs):
    if request.method == 'POST':
        # Get form data from the POST request
        data = {
            "title": request.POST.get('title'),
            "title_np": request.POST.get('title_np'),
            "trainee_name": request.POST.get('trainee_name'),
            "name_np": request.POST.get('name_np'),
            "father_name": request.POST.get('father_name'),
            "father_name_np": request.POST.get('father_name_np'),
            "date_of_birth_ad": request.POST.get('date_of_birth_ad'),
            "date_of_birth_bs": request.POST.get('date_of_birth_bs'),
            "district": request.POST.get('district'),
            "district_np": request.POST.get('district_np'),
            "municipality": request.POST.get('municipality'),
            "municipality_np": request.POST.get('municipality_np'),
            "ward_no": request.POST.get('ward_no'),
            "ward_no_np": request.POST.get('ward_no_np'),
            "training_name": request.POST.get('training_name'),
            "training_name_np": request.POST.get('training_name_np')
        }
        
        if 'image' in request.FILES:
            image = request.FILES['image']
            image_data = image.read()

            # Get MIME type of the image
            mime_type, _ = mimetypes.guess_type(image.name)

            # Convert image to base64 and include MIME type
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            data['image'] = f"data:{mime_type};base64,{image_base64}"
            
        if 'sponsor_image' in request.FILES:
            image = request.FILES['sponsor_image']
            image_data = image.read()

            # Get MIME type of the image
            mime_type, _ = mimetypes.guess_type(image.name)

            # Convert image to base64 and include MIME type
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            data['sponsor_image'] = f"data:{mime_type};base64,{image_base64}"

            # Debug: Check if the base64 string is being generated correctly

        # Render PDF using PDFKit
        # return HttpResponse(data['sponsor_image'])
    
        return renderers.render_to_pdf_pdfkit('pdfs/certificate/index.html', data) 
    
def pdf_view2(request, *args, **kwargs):
    if request.method == 'POST':
        # Get form data from the POST request
        data = {
                    'certificate_number': request.POST.get('certificate_number'),
                    'ctevt_account_number': request.POST.get('ctevt_account_number'),
                    'pan_number': request.POST.get('pan_number'),
                    'sponsor': request.POST.get('sponsor'),
                    'course': request.POST.get('course'),
                    'creditHr': request.POST.get('creditHr'),
                    'start_date': request.POST.get('start_date'),
                    'end_date': request.POST.get('end_date'),
                    'municipality': request.POST.get('municipality'),
                    'ward_no': request.POST.get('ward_no'),
                    'city': request.POST.get('city'),
                    'parents_name': request.POST.get('parents_name'),
                    'trainee_name': request.POST.get('trainee_name'),
                    'certified_date': request.POST.get('certified_date'),
                }
        
        if 'image' in request.FILES:
            image = request.FILES['image']
            image_data = image.read()

            # Get MIME type of the image
            mime_type, _ = mimetypes.guess_type(image.name)

            # Convert image to base64 and include MIME type
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            data['image'] = f"data:{mime_type};base64,{image_base64}"
            
        if 'sponsor_image1' in request.FILES:
            image = request.FILES['sponsor_image1']
            image_data = image.read()

            # Get MIME type of the image
            mime_type, _ = mimetypes.guess_type(image.name)

            # Convert image to base64 and include MIME type
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            data['sponsor_image1'] = f"data:{mime_type};base64,{image_base64}"
            
        if 'sponsor_image2' in request.FILES:
            image = request.FILES['sponsor_image2']
            image_data = image.read()

            # Get MIME type of the image
            mime_type, _ = mimetypes.guess_type(image.name)

            # Convert image to base64 and include MIME type
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            data['sponsor_image2'] = f"data:{mime_type};base64,{image_base64}"
            
        if 'sponsor_image3' in request.FILES:
            image = request.FILES['sponsor_image3']
            image_data = image.read()

            # Get MIME type of the image
            mime_type, _ = mimetypes.guess_type(image.name)

            # Convert image to base64 and include MIME type
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            data['sponsor_image3'] = f"data:{mime_type};base64,{image_base64}"

            # Debug: Check if the base64 string is being generated correctly

        # Render PDF using PDFKit
        # return HttpResponse(data['sponsor_image'])
    
        return renderers.render_to_pdf_pdfkit('pdfs/certificate/certificate_two.html', data) 