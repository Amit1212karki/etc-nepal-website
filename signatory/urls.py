from django.urls import path
from . import views

urlpatterns = [
    path('', views.signatoryIndex, name='signatory-index'),
    path('create/', views.signatoryCreate, name='signatory-create'),
    path('store/', views.signatoryStore, name='signatory-store'),
    path('edit-signatory/<int:id>/', views.signatoryEdit, name='signatory-edit'),
    path('update-signatory/<int:id>/', views.signatoryUpdate, name='signatory-update'),
    path('delete-signatory/<int:id>/', views.signatoryDelete, name='signatory-delete'),
]
