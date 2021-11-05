from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from website_users.models import FamilyProfile
from .models import LanguageSpecifier


def select_language_view(request, pk):
    """Add users to each other's connecions list when one user accepts
    the other user's connect request and remove the sender from the receiver's
    pending list.
    """
    profile_page = get_object_or_404(FamilyProfile, id=request.POST.get('profile_id_4'))

    request.user.familyprofile.pending_requests.remove(profile_page.user)
    request.user.familyprofile.connections.add(profile_page.user)
    profile_page.connections.add(request.user)

    return HttpResponseRedirect(reverse('pending-requests'))


def delete_connection_view(request, pk):
    """Remove users from each other's connections list when one user
    deletes the other user from their list.
    """
    profile_page = get_object_or_404(FamilyProfile, id=request.POST.get('profile_id_6'))    
    request.user.familyprofile.connections.remove(profile_page.user)
    profile_page.connections.remove(request.user)

    return HttpResponseRedirect(reverse('family-profile', args=[str(request.user.familyprofile.id)]))