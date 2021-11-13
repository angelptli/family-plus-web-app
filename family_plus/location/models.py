from django.db import models
from location.utils import define_usa_states
from website_users.models import FamilyProfile
from multiselectfield import MultiSelectField

class Location(models.Model):
    STATES = define_usa_states()

    user    = models.ForeignKey(FamilyProfile, null=True, on_delete=models.CASCADE, related_name="related_user")
    state   = MultiSelectField(null=True, choices=STATES)
    city    = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        """Return username."""
        return str(self.user)
