from django.db import models
from django.conf import settings
from django.urls import reverse


class FamilyProfile(models.Model):
    user           = models.OneToOneField(settings.AUTH_USER_MODEL, null=True,
                                          on_delete=models.CASCADE)
    family_name    = models.TextField(max_length=30, null=False, blank=False)
    profile_image  = models.ImageField(max_length=255, null=True, blank=True)
    family_bio     = models.TextField(null=True, blank=True)
    contact_info   = models.TextField(null=True, blank=True)
    hobbies        = models.TextField(null=True, blank=True)
    interests      = models.TextField(null=True, blank=True)
    locations      = models.TextField(null=True, blank=True)
    schedule       = models.TextField(null=True, blank=True)
    languages      = models.TextField(null=True, blank=True)
    family_members = models.TextField(null=True, blank=True)

    def __str__(self):
        """Label users by their username."""
        return self.username

    def get_absolute_url(self):
        return reverse('home')
