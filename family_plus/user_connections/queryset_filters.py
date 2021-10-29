# Filters queryset for specific search views
from custom_user_model.models import CustomUserModel
from website_users.models import FamilyProfile


def get_family_queryset(query=None):
    """Return queryset filtered by family name contained in search."""
    queries = query.split(" ")  # Remove spacing
    queryset = []

    for q in queries:
        search_results = FamilyProfile.objects \
                            .filter(family_name__icontains=q) \
                            .order_by('-has_setup')

        queryset = [result for result in search_results]

    return queryset


def get_username_queryset(query=None):
    """Return queryset filtered by family name contained in search."""
    queries = query.split(" ")  # Remove spacing
    queryset = []

    for q in queries:
        search_results = CustomUserModel.objects \
                            .filter(username__icontains=q) \
                            .order_by('-familyprofile__has_setup')

        queryset = [result for result in search_results]

    return queryset