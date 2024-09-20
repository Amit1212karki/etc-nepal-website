from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='course-index'),
    path('single-course/<int:id>/', singlePage, name='single-page')
]