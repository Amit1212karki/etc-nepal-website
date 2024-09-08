from django.urls import path
from .views import *



urlpatterns = [
    path('contact/', contact, name='contact'),
    path('store-contact/', storeContact, name='store-contact')
]