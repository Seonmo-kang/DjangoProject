"""DjangoProject_mvc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from appFolder import views
from rest_framework import routers



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('appFolder.urls')), # App 'appFolder' urls file must be in project server.
    path('frontend/',include('frontend.urls')), # React app called frontend
    # path('',include('appFolder.urls')) # if you want to direct app to main(128.0.0.1:8000/), then use this.
]
