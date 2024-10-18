from django.urls import path
from .views import *

urlpatterns = [
    path('', sponsorIndex, name='sponsor-index'),
    path('add-sponsor/', sponsorAdd, name='sponsor-add'),
    path('store-sponsor/', sponsorStore, name='sponsor-store'),
    path('edit-sponsor/<int:id>/', sponsorEdit, name='sponsor-edit'),
    path('update-sponsor/<int:id>/', sponsorUpdate, name='sponsor-update'),
    path('delete-sponsor/<int:id>/', sponsorDelete, name='sponsor-delete'),

]