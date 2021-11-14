"""family_plus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from location.views import (
    LocationLogView,
    AddLocationView,
    delete_location,
)

urlpatterns = [
    path('location/log/<str:user>/', LocationLogView.as_view(), name='location-log'),
    path('add_location/', AddLocationView.as_view(), name='add-location'),
    path('delete_location/log/<int:pk>/', delete_location, name='delete-location'),

]
