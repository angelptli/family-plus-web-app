from django.db import models
from django.conf import settings
from custom_user_model.models import get_profile_image_filepath
from django.urls import reverse


class FamilyProfile(models.Model):
    user           = models.OneToOneField(settings.AUTH_USER_MODEL, null=True,
                                          on_delete=models.CASCADE)
    family_name    = models.TextField(max_length=30, null=False, blank=False)
    profile_image  = models.ImageField(max_length=255, null=True, blank=True,
                                       upload_to=get_profile_image_filepath)
    family_bio     = models.TextField(null=True, blank=True)
    contact_info   = models.TextField(null=True, blank=True)
    hobbies        = models.TextField(null=True, blank=True)
    interests      = models.TextField(null=True, blank=True)
    locations      = models.TextField(null=True, blank=True)
    schedule       = models.TextField(null=True, blank=True)
    languages      = models.TextField(null=True, blank=True)
    family_members = models.TextField(null=True, blank=True)
    has_setup      = models.BooleanField(default=False)
    hidden         = models.BooleanField(default=False)

    def __str__(self):
        """Label users by their username."""
        return self.user.username

    def get_absolute_url(self):
        return reverse('home')

    def has_family_profile(self):
        """Used for verifying that the user has set up a family profile."""
        if self.familyprofile.family_name != "":
            self.familyprofile.has_setup = True
            self.familyprofile.save()

    def hide_profile(self, action):
        """Used for toggling hidden status on or off.

        Default is set to False. Pass in "toggle_on" to save as True or
        "toggle_off" to save as False. Users toggled on (True) won't show up
        in search results nor can they send or receive connect requests.
        """
        if action == "toggle_on":
            self.familyprofile.hidden = True
            self.familyprofile.save()
            return True
        elif action == "toggle_off":
            self.familyprofile.hidden = False
            self.familyprofile.save()
            return False