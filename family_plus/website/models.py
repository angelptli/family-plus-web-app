from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# class FamilyPlusUser(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=200)
#     password = models.CharField(max_length=50)
#     age = models.IntegerField()

#     def __str__(self):
#         """Label members by their full name in the db.

#         :return: member's first and last name 
#         :rtype: self objects
#         """
#         return self.first_name + ' ' + self.last_name


class FamilyProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True,
                                    upload_to="images/profile")
    family_bio = models.TextField(null=True, blank=True)
    contact_info = models.TextField(null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
    locations = models.TextField(null=True, blank=True)
    schedule = models.TextField(null=True, blank=True)
    languages = models.TextField(null=True, blank=True)
    family_members = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')