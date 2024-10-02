from django.urls import path
from . import views

urlpatterns = [
    path('', views.signatoryIndex, name='signatory-index'),
    path('create/', views.signatoryCreate, name='signatory-create'),
    path('store/', views.signatoryStore, name='signatory-store'),
    path('edit/<int:id>/', views.signatoryEdit, name='signatory-edit'),
    path('update/<int:id>/', views.signatoryUpdate, name='signatory-update'),
    path('delete/<int:id>/', views.signatoryDelete, name='signatory-delete'),
]
