from django.urls import path
from .views import *


urlpatterns = [
    path('', index , name='publication-index'),
    path('search-publications/', publication_list, name='publication_list'), 
]