from django.shortcuts import render
from .models import *
# Create your views here.

def Contact(request):
    return render(request, 'front/pages/contact.html')

