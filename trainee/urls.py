from django.urls import path
from . import views

urlpatterns = [
    path('', views.traineeIndex, name='trainee-index'),  # List all trainees
    path('add/', views.traineeCreate, name='trainee-create'),  # Show form to add a trainee
    path('store/', views.traineeStore, name='trainee-store'),  # Handle storing of a new trainee
    path('edit/<int:id>/', views.traineeEdit, name='trainee-edit'),  # Show form to edit a trainee
    path('update/<int:id>/', views.traineeUpdate, name='trainee-update'),  # Handle updating a trainee
    path('delete/<int:id>/', views.traineeDelete, name='trainee-delete'),  # Handle deletion of a trainee
]
