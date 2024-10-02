from django.urls import path
from .views import *

urlpatterns = [
    path('', traineeIndex, name='trainee-index'),
    path('add-trainee/', traineeCreate, name='trainee-create'),
    path('store-trainee/', traineeStore, name='trainee-store'),
    path('edit-trainee/<int:id>/', traineeEdit, name='trainee-edit'),
    path('update-trainee/<int:id>/', traineeUpdate, name='trainee-update'),
    path('delete-trainee/<int:id>/', traineeDelete, name='trainee-delete'),

]
