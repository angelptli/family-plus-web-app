# Filters queryset for specific search views
from custom_user_model.models import CustomUserModel
from website_users.models import FamilyProfile, FamilyMember
from hobby.models import Hobby
from location.models import Location
from language.models import Language
from availability.models import Availability
from django.db.models import Q


def get_family_queryset(query=None):
    """Return queryset filtered by family name contained in search."""
    queries = query.split(" ")  # Split query into list by space
    queryset = []

    for q in queries:
        search_results = FamilyProfile.objects \
                            .filter(family_name__icontains=q) \
                            .order_by('-has_setup')

        queryset = [result for result in search_results]

    return queryset


def get_username_queryset(query=None):
    """Return queryset filtered by family name contained in search."""
    queries = query.split(" ")  # Split query into list by space
    queryset = []

    for q in queries:
        search_results = CustomUserModel.objects \
                            .filter(username__icontains=q) \
                            .order_by('-familyprofile__has_setup')

        queryset = [result for result in search_results]

    return queryset


def get_hobby_queryset(query=None):
    """Filter queryset by chosen hobby and return a list of matching
    family profiles."""
    profiles = []
    results = Hobby.objects.filter(hobbies__icontains=query)
    # results = Hobby.objects.filter(hobbies=query)

    for result in results:
        search_results = FamilyProfile.objects \
                            .filter(user__username=result.user) \
                            .exclude(hidden=True)
        profiles = [result for result in search_results]

    return profiles


def get_location_queryset(query=None):
    """Filter queryset by chosen state and city and return a list of matching
    family profiles."""
    profiles = []
    results = Location.objects.filter(Q(state__icontains=query) | Q(city__icontains=query))

    for result in results:
        search_results = FamilyProfile.objects \
                            .filter(user__username=result.user) \
                            .exclude(hidden=True)
        profiles = [result for result in search_results]

    return profiles


def get_language_queryset(query=None):
    """Filter queryset by chosen language and return a list of matching
    family profiles."""
    profiles = []
    results = Language.objects.filter(languages__icontains=query)
    # results = Language.objects.filter(days=query)

    for result in results:
        search_results = FamilyProfile.objects \
                            .filter(user__username=result.user) \
                            .exclude(hidden=True)
        profiles = [result for result in search_results]

    return profiles


def get_day_queryset(query=None):
    """Filter queryset by chosen day and return a list of matching
    family profiles."""
    profiles = []
    results = Availability.objects.filter(days__icontains=query)
    # results = Availability.objects.filter(days=query)

    for result in results:
        search_results = FamilyProfile.objects \
                            .filter(user__username=result.user) \
                            .exclude(hidden=True)
        profiles = [result for result in search_results]

    return profiles


def get_age_range_queryset(query=None):
    """Filter queryset by chosen age range and return a list of
    matching family profiles."""
    profiles = []
    results = FamilyMember.objects.filter(age_range=query)

    for result in results:
        search_results = FamilyProfile.objects \
                            .filter(user__username=result.user) \
                            .exclude(hidden=True)
        profiles = [result for result in search_results]

    return profiles
