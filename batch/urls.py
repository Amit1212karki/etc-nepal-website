from django.urls import path
from .views import *


urlpatterns = [
    path('', batchIndex, name='batch-index'),
    path('add-batch/', batchCreate, name='batch-create'),
    path('store-batch/', batchStore, name='batch-store'),
    path('edit-batch/<int:id>/', batchEdit, name='batch-edit'),
    path('update-batch/<int:id>/', batchUpdate, name='batch-update'),
    path('delete-batch/<int:id>/', batchDelete, name='batch-delete'),
]