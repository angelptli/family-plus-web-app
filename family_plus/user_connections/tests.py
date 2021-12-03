from django.test import TestCase
from django.urls import reverse

from custom_user_model.models import CustomUserModel
from website_users.models import FamilyProfile
from hobby.models import Hobby
from user_connections.utils import (
    get_hobby_list,
    get_language_list,
    get_day_list,
    get_age_range_list
)


class UserConnectionsTests(TestCase):

    """Test user connections, statuses, and searching functions.
    
    Test that...
    - users are added to each others connections lists successfully
    - contact info is visible between connections but not non-connections
    - the correct search choices are displayed on the search page
    - the search results page shows the correct search results
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
        self.client.login(email='example4000@mail.com', password='alpaca4567')

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

    def test_search_choices(self):
        """Test that the search menus in the search page contain the correct
        choices used in the Hobby, Location, Language, and Availability models.
        """
        # Log in to User 1's account and go to the search page
        self.client.login(email='example3000@mail.com', password='alpaca4567')
        response = self.client.get(reverse('search-page'))
        self.assertEquals(response.status_code, 200)

        # Check that each word in the hobby list is present on the page
        for choice in get_hobby_list():
            for word in choice:
                self.assertContains(response, word)

        # Check that each word in the language list is present on the page
        for choice in get_language_list():
            for word in choice:
                self.assertContains(response, word)

        # Check that each word in the day list is present on the page
        for choice in get_day_list():
            for word in choice:
                self.assertContains(response, word)

        # Check that each word in the age range list is present on the page
        for choice in get_age_range_list():
            for word in choice:
                self.assertContains(response, word)

    def test_search_results(self):
        """Check that searching a category in the search page redirects to
        the correct results page and contains the correct search results.
        """
        # Create 5 user objects that are only accessible in this function
        # and add an hobby object for each
        for i in range(3, 8):
            username = 'example' + str(i) + 'xxx'
            email = username + '@mail.com'

            CustomUserModel.objects.create(email=email,
                                            username=username,
                                            password='alpaca4567',
                                            is_adult=True)

            user = CustomUserModel.objects.get(id=i)
            user.set_password('alpaca4567')
            user.save()

            family_name = 'Example ' + str(i) + 'xxx'
            FamilyProfile.objects.create(user=user,
                                        family_name=family_name)

            Hobby.objects.create(user=user.familyprofile, hobbies=['Baking'])

        # Log in to the first user's account made in this function
        self.client.login(email='example3xxx@mail.com', password='alpaca4567')

        # Visit search page
        response = self.client.get(reverse('search-page'))
        self.assertEquals(response.status_code, 200)

        # Search the 'Baking' hobby and confirm it takes us to the search
        # results page for hobbies
        response = self.client.post(reverse('search-hobby'), data={'value':'Baking'})
        self.assertTemplateUsed('results/search-hobby.html')
        self.assertEquals(response.status_code, 200)

        # Check that the users made in this function have their family
        # nicknames displayed
        for i in range(3, 8):
            self.assertContains(response, 'Example')
            self.assertContains(response, str(i))
            self.assertContains(response, 'xxx')
            self.assertContains(response, 'Family')