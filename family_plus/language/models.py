from django.db import models
from website_users.models import FamilyProfile
from language.utils import define_languages
from multiselectfield import MultiSelectField


class Language(models.Model):

    """Each family can select languages that they know or are generally
    interested in.
    """

    LANGUAGES = define_languages()

    user = models.OneToOneField(FamilyProfile, null=True, on_delete=models.CASCADE)
    languages = MultiSelectField(null=True, choices=LANGUAGES)

    def __str__(self):
        """Return user of language log object."""
        return str(self.user)
