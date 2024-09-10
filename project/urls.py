from django.urls import path
from .views import *


urlpatterns = [
    path('ongoing/', onGoing, name='ongoing-index'),
    path('single-ongoing-project/<int:id>/', singleOngoing , name='single-ongoing'),
    path('completed/', completed, name='completed-index'),
    path('single-completed-project/<int:id>/', singleCompleted , name='single-completed'),


]