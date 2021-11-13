from django.db import models
from website_users.models import FamilyProfile
from availability.utils import define_days
from multiselectfield import MultiSelectField


class Availability(models.Model):

    """Families can share when they are available to interact with other
    families.
    """

    DAYS = define_days()

    user   = models.OneToOneField(FamilyProfile, null=True, on_delete=models.CASCADE)
    days   = MultiSelectField(null=True, choices=DAYS)

    def __str__(self):
        """Return user of this object."""
        return str(self.user)