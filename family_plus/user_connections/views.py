from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from operator import attrgetter

# Imported models
from django.db.models import Q
from custom_user_model.models import CustomUserModel
from website_users.models import FamilyProfile
# from .models import ConnectionsList, ConnectRequest

# Imported filter functions
from .queryset_filters import (
    get_family_queryset,
    get_username_queryset,
)

# from .connect_status import ConnectStatus


def connections_view(request, *args, **kwargs):
    """Distinguish between the different types of connection states.
    
    The is_connection variable can be True or False, indicating whether
    another user is on the user's connection list. The is_self variable
    identifies the user's id.
    """

    # Credit: https://youtu.be/gGrca2uLYq0
    # Learned the concept of customizing context variables to represent
    # different states for granting different displays and displays to users

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
        
        # If profile viewer is logged in and is viewing someone else's
        # family profile, set is_self to False. Not logged in set to false.
        if user.is_authenticated and user != account:
            is_self = False
        elif not user.is_authenticated:
            is_self = False

        # Add variables to context dictionary
        context['is_self'] = is_self
        context['is_connection'] = is_connection
        context['BASE_URL'] = settings.BASE_URL  # localhost:8000 url

        return render(request, "family_profile/family-profile.html", context)

    # This is code that might be used for adding connections to users'
    # connection lists - YET TO BE MADE.
    if request.method == "GET":
        search_query = request.GET.get("q")

        # If user enters at least one character in the search box return a
        # query set of users who have emails and/or usernames that contain
        # the search text
        if len(search_query) > 0:
            search_results = CustomUserModel.objects.filter(
                email__icontains=search_query).filter(
                    username__icontains=search_query).distinct()

        # Connection status
        # user = request.user
        name_results = []
        for name in search_results:
            name_results.append((name, False))

        context['name_results'] = name_results


def search_page_view(request, *args, **kwargs):
    """This view hosts the search boxes of other views, providing a varierty
    of search criteria. Users can search by interest, location, language,
    age range, and/or availability. Users can also search by username or
    family name alone.
    """
    context = {}

    return render(request, "search/search-page.html", context)


def search_family_view(request, *args, **kwargs):
    """This view is for searching family names specifically."""

    # Credit: https://www.youtube.com/watch?v=YlMxfqcw77s
    # Learned how to paginate filtered objects and more on what
    # GET does as well as how to handle its exceptions.

    context = {}
    query = ""

    if request.GET:
        # Get value or no value passed in
        q = "familynameq"  # used in general paginator HTML code
        query = request.GET.get(q, '')

        context['q'] = q
        context['query'] = str(query)

    search_results = get_family_queryset(query)  

    # Paginate with a specified number of results on each page
    results_per_page = 8
    page_number = request.GET.get('page', 1)  # default of 1 result
    paginator = Paginator(search_results, results_per_page)
    
    # Try paginating with different numbers of results per page
    try:
        search_results = paginator.page(page_number)
    except PageNotAnInteger:
        search_results = paginator.page(results_per_page)  # specified number
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    context['search_results'] = search_results
    
    return render(request, "results/search-family.html", context)


def search_username_view(request, *args, **kwargs):
    """This view is for searching usernames specifically."""

    context = {}
    query = ""

    if request.GET:
        # Get value or no value passed in
        q = "usernameq"  # used in general paginator HTML code
        query = request.GET.get(q, '')

        context['q'] = q
        context['query'] = str(query)

    search_results = get_username_queryset(query)  

    # Paginate with a specified number of results on each page
    results_per_page = 8
    page_number = request.GET.get('page', 1)  # default of 1 result
    paginator = Paginator(search_results, results_per_page)
    
    # Try paginating with different numbers of results per page
    try:
        search_results = paginator.page(page_number)
    except PageNotAnInteger:
        search_results = paginator.page(results_per_page)  # specified number
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    context['search_results'] = search_results

    return render(request, "results/search-username.html", context)
