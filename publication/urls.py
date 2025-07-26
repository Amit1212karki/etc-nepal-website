from django.urls import path
from .views import *


urlpatterns = [
    path('', index , name='publication_list')
]