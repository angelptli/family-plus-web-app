from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FamilyProfile, FamilyMember


class CustomProfileAdmin(UserAdmin):

    """Custom admin set up for the FamilyProfile model."""

    ordering = ('id',)

    list_display = (
        'id',
        'user',
        'family_name'
    )

    search_fields = (
        'id',
        'user',
        'family_name',
        'hidden'
    )

    readonly_fields = (
    )

    # Turn off filters
    filter_horizontal = ()
    list_filter = ()
    fieldsets= ()

admin.site.register(FamilyProfile, CustomProfileAdmin)

admin.site.register(FamilyMember)
