from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from custom_user_model.models import CustomUserModel
from website_users.models import FamilyProfile
from .connect_status import ConnectStatus
from .models import ConnectionsList, ConnectRequest
from itertools import chain

def connections_view(request, *args, **kwargs):
    """Distinguish between the different types of connection states.
    
    The is_connection variable can be True or False, indicating whether
    another user is on the user's connection list. The is_self variable
    identifies the user's id.

    Credit: https://youtu.be/gGrca2uLYq0
    """
    context = {}

    # The id of the profile owner. Takes the id value from url.
    user_id = kwargs.get("user_id")

    # Check if the profile owner exists
    try:
        account = CustomUserModel.objects.get(pk=user_id)
    except CustomUserModel.DoesNotExist:
        return HttpResponse("That user doesn't exist.")

    # If user exists, add user's fields to context dictionary
    if account:
        context['id'] = account.id
        context['username'] = account.username
        context['email'] = account.email
        context['profile_image'] = account.profile_image.url
        context['hide_email'] = account.hide_email

        # Default states
        is_self = True
        is_connection = False
        user = request.user
        
        # If profile viewer is logged in and it is viewing someone else's
        # profile, set is_self to False
        if user.is_authenticated and user != account:
            is_self = False
        elif not user.is_authenticated:
            is_self = False

        # Add variables to context dictionary
        context['is_self'] = is_self
        context['is_connection'] = is_connection
        context['BASE_URL'] = settings.BASE_URL  # localhost:8000 url

        return render(request, "family_profile/family-profile.html", context)


def search_page_view(request, *args, **kwargs):
    context = {}
    # user_queryset = CustomUserModel.objects.all()
    # family_queryset = FamilyProfile.objects.all()

    if request.method == "POST":
        # searched = request.POST.get('searched')
        search_user = request.POST.get('user_searched')
        search_family = request.POST.get('family_searched')

        context['search_user'] = search_user
        context['search_family'] = search_family

        return render(request, "search/search-page.html", context)
    else:
        return render(request, "search/search-page.html", context)


def search_username_view(request, *args, **kwargs):
    """This view is for searching usernames specifically."""
    context = {}
    search_results = ""
    has_three_chars = True

    if request.method == "POST":
        searched_username = request.POST.get('search_user')

        if len(searched_username) < 3:
            has_three_chars = False

        context['searched_username'] = searched_username
        context['has_three_chars'] = has_three_chars
        
        if len(searched_username) > 0:
            search_results = CustomUserModel.objects.filter(
                    username__icontains=searched_username)
        
        context['search_results'] = search_results

        return render(request, "results/search-username.html", context)
    else:
        context['search_results'] = search_results
        return render(request, "results/search-username.html", context)


def search_family_view(request, *args, **kwargs):
    """This view is for searching family names specifically."""
    context = {}
    search_results = ""
    has_three_chars = True

    if request.method == "POST":
        searched_family = request.POST.get('search_family')

        if len(searched_family) < 3:
            has_three_chars = False

        context['searched_family'] = searched_family
        context['has_three_chars'] = has_three_chars
        
        if len(searched_family) > 0:
            search_results = FamilyProfile.objects.filter(
                    family_name__icontains=searched_family)
        
        context['search_results'] = search_results

        return render(request, "results/search-family.html", context)
    else:
        context['search_results'] = search_results
        return render(request, "results/search-family.html", context)

    # # This is code that might be used for adding connections to users'
    # # connection lists - YET TO BE MADE.
    # if request.method == "GET":
    #     search_query = request.GET.get("q")

    #     # If user enters at least one character in the search box return a
    #     # query set of users who have emails and/or usernames that contain
    #     # the search text
    #     if len(search_query) > 0:
    #         search_results = CustomUserModel.objects.filter(
    #             email__icontains=search_query).filter(
    #                 username__icontains=search_query).distinct()

    #     # Connection status
    #     # user = request.user
    #     name_results = []
    #     for name in search_results:
    #         name_results.append((name, False))

    #     context['name_results'] = name_results