from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from contract.models import *
from batch.models import *
from trainee.models import *
from trainer.models import *
from certificate.models import *

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
                messages.success(request, "You have been logged in successfully.")
                return render(request, 'certificate/home.html')
            else:
                messages.error(request,'Provided credintial is invalid !!')       
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
    return render(request, 'certificate/login.html')

@login_required
def home(request):
    home_contract = Contract.objects.count()
    home_batch = Batch.objects.count()
    home_trainer = Trainer.objects.count()
    home_trainee = Trainee.objects.count()
    home_certificate = Certificate.objects.count()
    context = {
        'home_contract':home_contract,
        'home_batch':home_batch,
        'home_trainer':home_trainer,
        'home_trainee':home_trainee,
        'home_certificate':home_certificate
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
    

