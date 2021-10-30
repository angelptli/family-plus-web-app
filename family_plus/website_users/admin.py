from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FamilyProfile


class CustomProfileAdmin(UserAdmin):

    """Custom admin set up for the FamilyProfile model."""

    ordering = ('id',)

    list_display = (
        'id',
        'user',
        'has_setup',
        'family_name',
        'profile_image',
        'family_bio',
        'contact_info'
    )

    search_fields = (
        'id',
        'user',
        'family_name',
        'family_bio',
        'hidden'
    )

    readonly_fields = (
    )

    # Turn off filters
    filter_horizontal = ()
    list_filter = ()
    fieldsets= ()

admin.site.register(FamilyProfile, CustomProfileAdmin)