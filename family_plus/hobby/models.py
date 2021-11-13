from django.db import models
from website_users.models import FamilyProfile
from hobby.utils import define_hobbies
from multiselectfield import MultiSelectField

class Hobby(models.Model):

    """Families can share their hobbies and interests."""

    HOBBIES = define_hobbies()

    user = models.OneToOneField(FamilyProfile, null=True, on_delete=models.CASCADE)
    hobbies   = MultiSelectField(null=True, choices=HOBBIES)
    other     = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        """Return user of this hobby log object."""
        return str(self.user)
