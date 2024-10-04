from django.urls import path
from .views import *

urlpatterns = [
     path('', loginPage, name='certificate-login-page'),
     path('login/', loginView, name='certificate-login'),
     path('logout/<int:id>/', logoutUser, name='certificate-logout'),
     path('dashboard/', home, name='certificate-home'),
     
     # certificate generation urls
     path('certificate-index/', certificatIndex, name='certificate-index'),
     path("certificate-form/", certificateForm ),
     path("certificate-form2/", certificateForm2 ),
     path("html-to-pdf/", pdf_view),
     path("html-to-pdf2/", pdf_view2),

    
]