from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='document-index')
]



