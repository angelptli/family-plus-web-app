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
from user_connections.views import (
    search_page_view,
    search_family_view,
    search_username_view,
    search_hobby_view,
    search_location_view,
    search_language_view,
    search_age_view,
    search_day_view,
    pending_requests_view,
    accept_request_view,
    decline_request_view,
    delete_connection_view,
)

urlpatterns = [
    path('search/', search_page_view, name="search-page"),
    path('families/search_results/', search_family_view, name="search-family"),
    path('users/search_results/', search_username_view, name="search-username"),
    path('hobbies/search_results/', search_hobby_view, name="search-hobby"),
    path('locations/search_results/', search_location_view, name="search-location"),
    path('languages/search_results/', search_language_view, name="search-language"),
    path('age_ranges/search_results/', search_age_view, name="search-age-range"),
    path('availability/search_results/', search_day_view, name="search-availability"),
    path('requests/', pending_requests_view, name="pending-requests"),
    path('accept_request/<int:pk>/', accept_request_view, name='accept-request'),
    path('decline_request/<int:pk>/', decline_request_view, name='decline-request'),
    path('delete_connection/<int:pk>/', delete_connection_view, name='delete-connection'),
]
