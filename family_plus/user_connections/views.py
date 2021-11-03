from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http.response import HttpResponseRedirect
from django.urls import reverse

# Import filter functions
from .queryset_filters import (
    get_family_queryset,
    get_username_queryset,
)


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


def pending_requests_view(request, *args, **kwargs):
    """Pending requests page view."""
    return render(request, 'requests/pending-requests.html', {})


# def send_request_view(request, pk):
#     """Add sender to receiver's pending list when sender sends a request
#     to connect.
#     """
#     return HttpResponseRedirect(reverse('family-profile', args=[str(pk)]))
