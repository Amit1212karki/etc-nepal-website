from django.urls import path
from .views import *

urlpatterns = [

    path('', trainerIndex, name='trainer-index'),
    path('add-trainer/', trainerCreate, name='trainer-create'),
    path('store-trainer/', trainerStore, name='trainer-store'),
    path('edit-trainer/<int:id>/', trainerEdit, name='trainer-edit'),
    path('update-trainer/<int:id>/', trainerUpdate, name='trainer-update'),
    path('delete-trainer/<int:id>/', trainerDelete, name='trainer-delete'),

]