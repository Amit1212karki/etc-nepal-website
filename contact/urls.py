from django.urls import path
from .views import *



urlpatterns = [
    path('contact/', Contact, name='see-contact')


]