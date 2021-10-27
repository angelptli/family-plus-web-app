from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from custom_user_model.models import CustomUserModel
from website_users.models import FamilyProfile
from .connect_status import ConnectStatus
from .models import ConnectionsList, ConnectRequest

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

    if request.method == "POST":
        searched = request.POST.get('searched')
        context['searched'] = searched
        return render(request, "search/search-page.html", context)
    else:
        return render(request, "search/search-page.html", context)


def search_names_view(request, *args, **kwargs):
    """This view is for searching family names and @usernames specifically."""
    context = {}
    search_results = ""
    has_three_chars = True

    if request.method == "POST":
        searched = request.POST.get('searched')

        if len(searched) < 3:
            has_three_chars = False

        context['searched'] = searched
        context['has_three_chars'] = has_three_chars
        
        if len(searched) > 0:
            search_results = FamilyProfile.objects.filter(
                    family_name__icontains=searched)
        
        context['search_results'] = search_results

        return render(request, "results/search-name.html", context)
    else:
        context['search_results'] = search_results
        return render(request, "results/search-name.html", context)

    # # GET requests are executed when a user enters text into the search bar
    # # and presses the enter key button or clicks the search icon button
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