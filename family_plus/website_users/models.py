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
    AGE_RANGE = (
        ('On the way', 'On the way'),
        ('Baby (0-12 months old)', 'Baby (0-12 months old)'),
        ('Toddler (1-3 years old)', 'Toddler (1-3 years old)'),
        ('Preschooler (3-5 years old)', 'Preschooler (3-5 years old)'),
        ('Gradeschooler (5-12 years old)', 'Gradeschooler (5-12 years old)'),
        ('Teenager (12-17 years old)', 'Teenager (12-17 years old)'),
        ('Adult (18-24 years old)', 'Adult (18-24 years old)'),
        ('Adult (25-29 years old)', 'Adult (25-29 years old)'),
        ('Adult (30-34 years old)', 'Adult (30-34 years old)'),
        ('Adult (35-39 years old)', 'Adult (35-39 years old)'),
        ('Adult (40-44 years old)', 'Adult (40-45 years old)'),
        ('Adult (45-49 years old)', 'Adult (45-49 years old)'),
        ('Adult (50-54 years old)', 'Adult (50-54 years old)'),
        ('Adult (55-59 years old)', 'Adult (55-59 years old)'),
        ('Adult (60-64 years old)', 'Adult (60-64 years old)'),
        ('Older Adult (65-69 years old)', 'Older Adult (65-69 years old)'),
        ('Older Adult (70-74 years old)', 'Older Adult (70-74 years old)'),
        ('Older Adult (75-79 years old)', 'Older Adult (75-79 years old)'),
        ('Older Adult (80-84 years old)', 'Older Adult (80-84 years old)'),
        ('Older Adult (85-89 years old)', 'Older Adult (85-89 years old)'),
        ('Older Adult (90-94 years old)', 'Older Adult (90-94 years old)'),
        ('Older Adult (95-99 years old)', 'Older Adult (95-99 years old)'),
        ('Older Adult (100+ years old)', 'Older Adult (100+ years old)'),
        ('Older Adult (90-94 years old)', 'Older Adult (90-94 years old)'),
        ('Choose not to share', 'Choose not to share')
    )

    RELATION = (
        ('Mother', 'Mother'),
        ('Father', 'Father'),
        ('Daughter', 'Daughter'),
        ('Son', 'Son'),
        ('Aunt', 'Aunt'),
        ('Uncle', 'Uncle'),
        ('Cousin', 'Cousin'),
        ('Parent', 'Parent'),
        ('Guardian', 'Guardian'),
        ('Foster Mother', 'Foster Mother'),
        ('Foster Father', 'Foster Father'),
        ('Foster Parent', 'Foster Parent'),
        ('Grandmother', 'Grandmother'),
        ('Grandfather', 'Grandfather'),
        ('Grandparent', 'Grandparent'),
        ('Relative', 'Relative'),
        ('Relative-In-Law', 'Relative-In-Law'),
        ('Family Friend', 'Family Friend'),
        ('Other', 'Other'),
    )

    user       = models.ForeignKey(FamilyProfile, null=True, on_delete=models.CASCADE, related_name="family_member")
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name  = models.CharField(max_length=30, null=True, blank=True)
    relation   = models.CharField(max_length=50, null=True, blank=True, choices=RELATION)
    age_range  = models.CharField(max_length=100, null=True, blank=True, choices=AGE_RANGE)
    about      = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        """Return label username | Log ID: #.
        
        Log ID is the object's id in the databse and does not represent
        of the number of family member objects a user adds to the databse.
        """
        return str(self.user) + ' | Log ID: ' + str(self.id)
