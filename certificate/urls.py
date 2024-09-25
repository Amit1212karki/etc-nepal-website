from django.urls import path
from .views import *

urlpatterns = [
     path("", login, name="certificate-login"),
     path("dashboard/", home, name="certificate-home"),
]