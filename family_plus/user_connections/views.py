from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from website_users.models import FamilyProfile

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
    """Display the user's received requests and the total number of received
    requests that are pending.
    """
    context = {}
    
    received_requests = request.user.familyprofile.pending_requests.all
    context['received_requests'] = received_requests

    # A user's total number of requests they have received and are
    # still pending for their response
    total_pending = request.user.familyprofile.total_pending()
    context['total_pending'] = total_pending

    return render(request, 'requests/pending-requests.html', context)


def send_request_view(request, pk):
    """Add sender to receiver's pending list when sender sends a request
    to connect.
    """
    profile_page = get_object_or_404(FamilyProfile, id=request.POST.get('profile_id_2'))
    profile_page.pending_requests.add(request.user)

    return HttpResponseRedirect(reverse('family-profile', args=[str(pk)]))


def cancel_request_view(request, pk):
    """Remove the sender from the receiver's pending list when the
    sender cancels the request.
    """
    profile_page = get_object_or_404(FamilyProfile, id=request.POST.get('profile_id_3'))
    profile_page.pending_requests.remove(request.user)

    return HttpResponseRedirect(reverse('family-profile', args=[str(pk)]))


def accept_request_view(request, pk):
    """Add users to each other's connecions list when one user accepts
    the other user's connect request and remove the sender from the receiver's
    pending list.
    """
    profile_page = get_object_or_404(FamilyProfile, id=request.POST.get('profile_id_4'))

    request.user.familyprofile.pending_requests.remove(profile_page.user)
    request.user.familyprofile.connections.add(profile_page.user)
    profile_page.connections.add(request.user)

    return HttpResponseRedirect(reverse('pending-requests'))


def decline_request_view(request, pk):
    """Remove the sender from the receiver's pending list when the
    receiver declines the request.
    """
    profile_page = get_object_or_404(FamilyProfile, id=request.POST.get('profile_id_5'))
    request.user.familyprofile.pending_requests.remove(profile_page.user)

    return HttpResponseRedirect(reverse('pending-requests'))


def delete_connection_view(request, pk):
    """Remove users from each other's connections list when one user
    deletes the other user from their list.
    """
    profile_page = get_object_or_404(FamilyProfile, id=request.POST.get('profile_id_6'))    
    request.user.familyprofile.connections.remove(profile_page.user)
    profile_page.connections.remove(request.user)

    return HttpResponseRedirect(reverse('family-profile', args=[str(request.user.familyprofile.id)]))
