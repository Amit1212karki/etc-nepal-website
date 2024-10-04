
from django.shortcuts import render
from etcportfolio import renderers
from notice.models import *
from project.models import *
from news.models import *
from partners.models import *
from records.models import *
from course.models import *
from django.template.loader import get_template
from django.http import HttpResponse
from signatory.models import Signatory




def index(request):
    home_notice = Notice.objects.all()
    home_project_ongoing = Project.objects.filter(status='Ongoing')[:3]
    home_project_completed = Project.objects.filter(status='Complete')[:3]
    home_news = News.objects.all()[:4]
    home_partner = Partner.objects.all()
    home_items = SuccessHistory.objects.filter(is_active=True)
    home_course = Course.objects.all()[:4]

    context = {
        'notice':home_notice,
        'project_ongoing': home_project_ongoing,
        'project_completed': home_project_completed,
        'news':home_news,
        'partner':home_partner,
        'success_items':home_items,
        'home_course':home_course
    }
    return render(request,'front/pages/homepage.html', context)

def about(request):
    return render(request, 'front/pages/about.html')


def vission(request):
    return render(request, 'front/pages/vission.html')

def mission(request):
    return render(request, 'front/pages/mission.html')

def goal(request):
    return render(request, 'front/pages/goal.html')

def hrDiagram(request):
    return render(request, 'front/pages/hrdiagram.html')

def objective(request):
    return render(request, 'front/pages/objective.html')


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