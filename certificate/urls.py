from django.urls import path
from .views import *

urlpatterns = [
     path('', loginPage, name='certificate-login-page'),
     path('login/', loginView, name='certificate-login'),
     path('logout/<int:id>/', logoutUser, name='certificate-logout'),
     path("dashboard/", home, name="certificate-home"),
     path("contract/", contractIndex, name="contract-index"),
     path("contract/add/", contractCreate, name="contract-create"),
     path("contract/edit/", contractEdit, name="contract-edit"),
     path("batch/", batchIndex, name="batch-index"),
     path("batch/add/", batchCreate, name="batch-create"),
     path("batch/edit/", batchEdit, name="batch-edit"),
     path("trainer/", trainerIndex, name="trainer-index"),
     path("trainer/add/", trainerCreate, name="trainer-create"),
     path("trainer/edit/", trainerEdit, name="trainer-edit"),
     path("trainee/", traineeIndex, name="trainee-index"),
     path("trainee/add/", traineeCreate, name="trainee-create"),
     path("trainee/edit/", traineeEdit, name="trainee-edit"),
]