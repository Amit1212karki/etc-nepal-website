from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "back/login.html")

def home(request):
    return render(request, "back/home.html")

def contractIndex(request):
    return render(request, "back/contract/index.html")

def contractEdit(request):
    return render(request, "back/contract/edit.html")

def contractCreate(request):
    return render(request, "back/contract/add.html")


def batchIndex(request):
    return render(request, "back/batch/index.html")

def batchEdit(request):
    return render(request, "back/batch/edit.html")

def batchCreate(request):
    return render(request, "back/batch/add.html")



def trainerIndex(request):
    return render(request, "back/trainer/index.html")

def trainerEdit(request):
    return render(request, "back/trainer/edit.html")

def trainerCreate(request):
    return render(request, "back/trainer/add.html")



def traineeIndex(request):
    return render(request, "back/trainee/index.html")

def traineeEdit(request):
    return render(request, "back/trainee/edit.html")

def traineeCreate(request):
    return render(request, "back/trainee/add.html")