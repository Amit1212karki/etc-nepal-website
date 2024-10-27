from django.urls import path
from .views import *


urlpatterns = [
    path('', admissionForm, name='admission-index'),
    path('store-admission/', admissionStore, name='admission-store'),

    
]