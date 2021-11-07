from django.db import models
from website_users.models import FamilyProfile


class Availability(models.Model):

    """Families can share when they are available to interact with other
    families.
    """

    DAY = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ('Weekdays', 'Weekdays'),
        ('Weekends', 'Weekends'),
    )
    
    TIME_OF_DAY = (
        ('Morning', 'Morning'),
        ('Noon', 'Noon'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
        ('Night', 'Night'),
        ('Anytime', 'Anytime'),
        ('Unknown', 'Unknown'),
    )

    user   = models.OneToOneField(FamilyProfile, null=False, on_delete=models.CASCADE)
    days        = models.CharField(max_length=255, null=True, choices=DAY)
    time_of_day = models.CharField(max_length=255, null=True, choices=TIME_OF_DAY)

    def __str__(self):
        """Label as Family # | Member #."""
        return str(self.user) + 'Availability'