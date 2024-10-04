from django.urls import path
from .views import *

urlpatterns = [
     path('', loginPage, name='certificate-login-page'),
     path('login/', loginView, name='certificate-login'),
     path('logout/<int:id>/', logoutUser, name='certificate-logout'),
     path('dashboard/', home, name='certificate-home'),
     
     path("certificate-form/", certificateForm ),
     path("certificate-form2/", certificateForm2 ),
     path("certificate-form3/", certificateForm3 ),
    
]