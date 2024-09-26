from django.urls import path
from .views import *

urlpatterns = [
     path('', loginPage, name='certificate-login-page'),
     path('login/', loginView, name='certificate-login'),
     path('dashboard/', loginView, name='certificate-login-dashboard'),

]