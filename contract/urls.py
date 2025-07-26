from django.urls import path
from .views import *

urlpatterns = [
    path('', contractIndex, name='contract-index'),
     path('add-contract/', contractCreate, name='contract-create'),
     path('store-contract/', contractStore, name='contract-store'),
     path('edit-contract/<int:id>/', contractEdit, name='contract-edit'),
     path('update-contract/<int:id>/', contractUpdate, name='contract-update'),
     path('delete-contract/<int:id>/', contractDelete, name='contract-delete'),
]