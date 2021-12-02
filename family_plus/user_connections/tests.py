from django.test import TestCase, Client
from django.urls import reverse


from custom_user_model.models import CustomUserModel
from website_users.models import FamilyProfile


class UserConnectionsTests(TestCase):

    """Create users and a family profile for each. Then test that each user
    has been created and a profile picture upload was optional. And test that
    another user's contact info is displayed only when two users are in
    each other's connections lists.
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

        self.familyprofile1 = FamilyProfile.objects.get(user=self.user1)
        self.familyprofile2 = FamilyProfile.objects.get(user=self.user2)

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

    def test_contact_info_visibility(self):
        """Check that another user's contact info becomes visible after
        becoming a connection.
        """
        # Add contact info to user1's family profile
        contact_info_user1 = 'Contact us via phone call at 1-555-5555'
        self.familyprofile1.contact_info = contact_info_user1
        self.familyprofile1.save()

        # Log into User 2's account
        login = self.client.login(email='example4000@mail.com',
                                  password='alpaca4567')

        # Visit User 1's family profile and confirm that there is no
        # contact info displayed
        response = self.client.get(reverse('family-profile', kwargs={'pk': self.familyprofile1.pk}))
        self.assertNotContains(response, contact_info_user1)

        # Add the users to each other's connection lists
        self.familyprofile1.connections.add(self.familyprofile2.user)
        self.familyprofile2.connections.add(self.familyprofile1.user)
        
        # Refresh page to see User 1's contact info displayed
        response = self.client.get(reverse('family-profile', kwargs={'pk': self.familyprofile1.pk}))
        self.assertContains(response, contact_info_user1)