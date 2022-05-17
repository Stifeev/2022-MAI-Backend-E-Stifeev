"""filmapp_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from filmapp import views

from filmapp.views import FilmViewSet, DirectorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("jango/api/film", FilmViewSet, basename="films")
router.register("api/film", FilmViewSet, basename="films")

router.register("jango/api/director", DirectorViewSet, basename="directors")
router.register("api/director", DirectorViewSet, basename="directors")

urlpatterns = [
    path("jango/", views.index, name='home'),
    path("", views.index, name='home'),
    
    
    path("jango/admin/", admin.site.urls),
    path("admin/", admin.site.urls),
]

urlpatterns += router.urls
