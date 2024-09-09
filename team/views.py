from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    all_team = Team.objects.all()
    context = {
        'team':all_team
    }
    return render(request,'front/pages/teams.html', context)