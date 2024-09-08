from django.shortcuts import render , redirect
from .models import *
from django.conf import settings
from django.contrib import messages
from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


# Create your views here.

def contact(request):
    recaptcha_site_key = settings.RECAPTCHA_PUBLIC_KEY
    return render(request, 'front/pages/contact.html', {'recaptcha_site':recaptcha_site_key})


def storeContact(request):
    if request.method == 'POST':
        # Validate reCAPTCHA
        captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
        captcha_response = request.POST.get('g-recaptcha-response')
        try:
            captcha.clean(captcha_response)
        except forms.ValidationError:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('contact-index')
        
        # Process other form data
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            newContact = Contact(
                name= name,
                email = email,
                phone = phone,
                subject = subject,
                message = message
            )
            newContact.save()
        except Exception as e:
            print(e)
            messages.error(request, 'An error occurred while saving the Contact.')
            return redirect('contact')

        return redirect('contact')  # Replace with appropriate redirect after successful form submission

    return render(request, 'front/pages/contact.html')    
