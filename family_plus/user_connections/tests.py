from django.test import TestCase, Client
from django.urls import reverse


from custom_user_model.models import CustomUserModel
from website_users.models import FamilyProfile


class UserConnectionsTests(TestCase):

    """Create users and a family profile for each. Then test that each user
    has been created and a profile picture upload was optional.
    """

    def setUp(self):
        """Create two user objects and then create a family profile for each."""
        CustomUserModel.objects.create(email='example3000@mail.com',
                                       username='example3000',
                                       password='alpaca4567',
                                       is_adult=True)
                                       
        CustomUserModel.objects.create(email='example4000@mail.com',
                                       username='example4000',
                                       password='alpaca4567',
                                       is_adult=True)

        self.user1 = CustomUserModel.objects.get(id=1)
        self.user2 = CustomUserModel.objects.get(id=2)

        self.user1.set_password('alpaca4567')
        self.user2.set_password('alpaca4567')
        self.user1.save()
        self.user2.save()

        FamilyProfile.objects.create(user=self.user1,
                                     family_name='Example 3000')

        FamilyProfile.objects.create(user=self.user2,
                                     family_name='Example 4000')

    def test_connection_added(self):
        """Make user1 and user2 connections and confirm that they are in
        each other's connections lists. 
        """
        familyprofile1 = FamilyProfile.objects.get(user=self.user1)
        familyprofile2 = FamilyProfile.objects.get(user=self.user2)

        # Add the users to each other's connection lists
        familyprofile1.connections.add(familyprofile2.user)
        familyprofile2.connections.add(familyprofile1.user)

        # Check that they are in each other's connection lists
        connection1 = familyprofile1.connections.all()[0]
        connection2 = familyprofile2.connections.all()[0]
        self.assertEquals(familyprofile2.user, connection1)
        self.assertEquals(familyprofile1.user, connection2)
