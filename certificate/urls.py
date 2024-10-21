from django.urls import path
from .views import *

urlpatterns = [
     path('', loginPage, name='certificate-login-page'),
     path('login/', loginView, name='certificate-login'),
     path('logout/<int:id>/', logoutUser, name='certificate-logout'),
     path('dashboard/', home, name='certificate-home'),
     
     # certificate generation urls
     path('certificate-index/', certificateFormGenerate, name='certificate-index'),

     # certificate axios url 
     path('get-batch-from-contract/<int:id>/',get_batch_from_contract),
     path('get-student-from-batch/<int:id>/',get_student_from_batch),
     path('generate/',generate_certificate)


     

]