from django.db import models
from location.utils import define_usa_states
from website_users.models import FamilyProfile

class Location(models.Model):
    STATES = define_usa_states()

    user  = models.ForeignKey(FamilyProfile, null=True, on_delete=models.CASCADE, related_name="related_user")
    state = models.CharField(max_length=15, null=True, blank=True, choices=STATES)
    city  = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        """Return username."""
        return str(self.user)
