from django.shortcuts import render

# Create your views here.
def onGoing(request):
    return render(request,'front/pages/ongoing_projects.html')

def completed(request):
    return render(request,'front/pages/completed_projects.html')