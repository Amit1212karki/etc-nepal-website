"""
URL configuration for etcportfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls')),
    path('', index),
    path('about/', about, name='about'),
    path('vission/', vission, name='vission'),
    path('mission/', mission, name='mission'),
    path('goal/', goal, name='goal'),
    path('objective/', objective, name='objective'),
    path('hr-diagram/', hrDiagram, name='hr-diagram'),
    path('publications/', include('publication.urls')),
    path('news/', include('news.urls')),
    path('projects/', include('project.urls')),
    path('notice/', include('notice.urls')),
    path('teams/', include('team.urls')),
    path('image/', include('image.urls')),
    path('video/', include('video.urls')),
    path('etc_document/', include('document.urls')),
    path('course/', include('course.urls')),
    path('certificate/', include('certificate.urls')),
    path('contract/', include('contract.urls')),
    path('trainer/', include('trainer.urls')),
    path('batch/', include('batch.urls')),
    path("signatory/", include("signatory.urls")),
    path("trainee/", include("trainee.urls")),
    path("html-to-pdf/", pdf_view),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)