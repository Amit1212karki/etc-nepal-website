from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='news-index'),
    path('single-news/<int:id>/', singlePage, name='single-page')
]