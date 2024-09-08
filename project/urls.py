from django.urls import path
from .views import *


urlpatterns = [
    path('ongoing/', onGoing),
    path('completed/', completed)

]