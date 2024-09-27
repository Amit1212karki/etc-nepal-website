from django.urls import path
from .views import *

urlpatterns = [
     path('', loginPage, name='certificate-login-page'),
     path('login/', loginView, name='certificate-login'),
     path('logout/<int:id>/', logoutUser, name='certificate-logout'),
     path('dashboard/', home, name='certificate-home'),
     
     path('trainee/', traineeIndex, name='trainee-index'),
     path('trainee/add/', traineeCreate, name='trainee-create'),
     path('trainee/edit/', traineeEdit, name='trainee-edit'),
]