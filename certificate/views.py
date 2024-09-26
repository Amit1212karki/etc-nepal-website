from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
                return render(request, 'certificate/home.html')
            else:
                messages.error(request,'Provided credintial is invalid !!')       
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
    return render(request, 'certificate/login.html')

login_required
def home(request):
    return render(request, 'certificate/home.html')
