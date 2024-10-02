from django.urls import path
from .views import *

urlpatterns = [
    path('', traineeIndex, name='trainee-index'),
     path('add-trainee/', traineeCreate, name='trainee-create'),
     path('store-trainee/', traineeStore, name='trainee-store'),
     path('edit-trainee/', traineeEdit, name='trainee-edit'),
]
