from django.db import models
from django.conf import settings
from custom_user_model.models import get_profile_image_filepath
from django.urls import reverse


class FamilyProfile(models.Model):
    user             = models.OneToOneField(settings.AUTH_USER_MODEL, null=True,
                                          on_delete=models.CASCADE)
    family_name      = models.TextField(max_length=30, null=False, blank=False)
    profile_image    = models.ImageField(max_length=255, null=True, blank=True,
                                       upload_to=get_profile_image_filepath)
    family_bio       = models.TextField(null=True, blank=True)
    contact_info     = models.TextField(null=True, blank=True)
    locations        = models.CharField(max_length=100, null=True, blank=True)
    has_setup        = models.BooleanField(default=False)
    hidden           = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="toggled_profiles")
    pending_requests = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="requests_pending")
    connections      = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="connections")

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

    def profile_hidden(self):
        """Return the status of the profile visibility. 1 for hidden and
        0 for not hidden."""
        return self.hidden.count()

    def total_pending(self):
        """Keep count of each user's received requests that are still
        pending for an action response."""
        return self.pending_requests.count()


class FamilyMember(models.Model):
    user       = models.ForeignKey(FamilyProfile, null=False, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False)
    last_name  = models.CharField(max_length=50, null=True)
    about      = models.CharField(max_length=255, null=True)

    def __str__(self):
        return 'Family ' + str(self.user.id) + ' | Member ' + str(self.id)