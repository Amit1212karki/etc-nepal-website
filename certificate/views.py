from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
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

@login_required
def home(request):
    return render(request, 'certificate/home.html')

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
def traineeIndex(request):
    return render(request, 'certificate/trainee/index.html')

@login_required
def traineeEdit(request):
    return render(request, 'certificate/trainee/edit.html')

@login_required
def traineeCreate(request):
    return render(request, 'certificate/trainee/add.html')
