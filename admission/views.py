from django.shortcuts import render, redirect, get_object_or_404
from location.models import *
from dateutil import parser
from .models import *
from django.contrib import messages
from django.conf import settings


# Create your views here.

def admissionForm(request):
    province = Province.objects.all()
    district = District.objects.all()
    palika = Palika.objects.all()
    recaptcha_site_key = settings.RECAPTCHA_PUBLIC_KEY

    context = {
        'province':province,
        'district':district,
        'palika':palika,
        'recaptcha_site':recaptcha_site_key
    }
    return render(request, 'front/pages/admission.html', context)


def admissionStore(request):
    if request.method == 'POST':
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

        
        province = get_object_or_404(Province, id=province_id)
        district = get_object_or_404(District, id=district_id)
        palika = get_object_or_404(Palika, id=palika_id)

        store_admission = Admission.objects.create(
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
        )

        store_admission.save()
        messages.success(request, 'Admission added successfully')
        return redirect('admission-index')
    else:
        messages.error(request,'Something went wrong!!')
    return render(request, 'front/pages/admission.html')

