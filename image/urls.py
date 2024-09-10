from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='image-index'),
    path('image/<int:id>/', singlePageImage, name="single-image")

]