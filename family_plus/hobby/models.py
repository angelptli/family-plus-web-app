from django.db import models
from website_users.models import FamilyProfile
from hobby.utils import define_hobbies

class Hobby(models.Model):

    """Families can share their hobbies and interests."""

    HOBBIES = define_hobbies()

    user = models.OneToOneField(FamilyProfile, null=False, on_delete=models.CASCADE)
    hobbies   = models.CharField(max_length=30, null=True, choices=HOBBIES)
    other     = models.CharField(max_length=255, null=True)

    def __str__(self):
        """Label as Family # | Member #."""
        return 'Family ' + str(self.user) + ' | Hobbies'
