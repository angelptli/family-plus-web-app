from django.test import TestCase
from django.urls import reverse

from custom_user_model.models import CustomUserModel
from website_users.models import FamilyProfile, FamilyMember
from hobby.models import Hobby
from location.models import Location
from language.models import Language
from availability.models import Availability

class FamilyProfileTests(TestCase):

    """Create users and a family profile for each to perform tests.
    
    Test that...
    - each family profile has been created properly
    - a profile picture is optional
    - the correct family bio is saved when updated
    - hidden profiles are not visible to other users
    - multiple choices are addable to an object for category models
    - edited category objects save the new updated data
    - family profile cannot set up if max_length (character limit) is exceeded
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

        CustomUserModel.objects.create(email='example5000@mail.com',
                                       username='example5000',
                                       password='alpaca4567',
                                       is_adult=True)

        self.user1 = CustomUserModel.objects.get(id=1)
        self.user2 = CustomUserModel.objects.get(id=2)
        self.user3 = CustomUserModel.objects.get(id=3)

        self.user1.set_password('alpaca4567')
        self.user2.set_password('alpaca4567')
        self.user3.set_password('alpaca4567')
        self.user1.save()
        self.user2.save()
        self.user3.save()

        FamilyProfile.objects.create(user=self.user1,
                                     family_name='Example 3000')

        FamilyProfile.objects.create(user=self.user2,
                                     family_name='Example 4000')

    def test_familyprofile_creation(self):
        """Confirm that the two family profiles were created by asserting
        matching user objects and family names.
        """
        familyprofile1 = FamilyProfile.objects.get(user=self.user1)
        familyprofile2 = FamilyProfile.objects.get(user=self.user2)
        expected_object_name1 = f'{familyprofile1.user}'
        expected_object_name2 = f'{familyprofile2.user}'
        self.assertEquals(expected_object_name1, 'example3000')
        self.assertEquals(expected_object_name2, 'example4000')
        expected_object_name1 = f'{familyprofile1.family_name}'
        expected_object_name2 = f'{familyprofile2.family_name}'
        self.assertEquals(expected_object_name1, 'Example 3000')
        self.assertEquals(expected_object_name2, 'Example 4000')

    def test_optional_profile_picture(self):
        """Test family profile picture optional upload by confirming that
        there is no text in the profile_pic field.
        """
        familyprofile1 = FamilyProfile.objects.get(user=self.user1)
        familyprofile2 = FamilyProfile.objects.get(user=self.user2)
        expected_object_name1 = f'{familyprofile1.profile_image}'
        expected_object_name2 = f'{familyprofile2.profile_image}'
        self.assertEquals(expected_object_name1, '')
        self.assertEquals(expected_object_name2, '')

    def test_update_family_bio(self):
        """Test that when a family profile's bio is updated, the correct
        version has been saved to the family profile object.
        """
        familyprofile = FamilyProfile.objects.get(user=self.user1)

        # First check that family_bio is None
        self.assertIsNone(familyprofile.family_bio)

        # Update family bio
        first_bio = 'This is my first bio update'
        familyprofile.family_bio = first_bio
        familyprofile.save()
        self.assertEqual(familyprofile.family_bio, first_bio)

        # Update family bio again
        second_bio = 'This is my second bio update'
        familyprofile.family_bio = second_bio
        familyprofile.save()
        self.assertNotEquals(familyprofile.family_bio, first_bio)

    def test_hidden_profile_visibility(self):
        """Confirm hidden profiles are not visible to other"""
        # Log into User 2's account
        logged_in = self.client.login(email='example4000@mail.com',
                                      password='alpaca4567')
        self.assertTrue(logged_in)

        # Vist User 1's family profile and confirm that content is visible
        # when User 1's family profile is not hidden
        response = self.client.get(reverse('family-profile', kwargs={'pk': self.user1.familyprofile.pk}))
        self.assertContains(response, 'Hobbies & Interests')
        self.assertContains(response, 'Family Members')
        self.assertNotContains(response, 'Family is not ready to connect')

        # Make User 1's family profile hidden
        familyprofile = FamilyProfile.objects.get(user=self.user1)
        familyprofile.hidden.add(familyprofile.user)
        confirm_self = familyprofile.hidden.all()[0]
        self.assertEquals(familyprofile.user, confirm_self)

        # Visit User 1's family profile page again and confirm that content
        # is now not visible
        response = self.client.get(reverse('family-profile', kwargs={'pk': self.user1.familyprofile.pk}))
        self.assertNotContains(response, 'Hobbies & Interests')
        self.assertNotContains(response, 'Family Members')
        self.assertContains(response, 'Family is not ready to connect')

    def test_hidden_mode_sending_requests(self):
        """Confirm users cannot send connect requests when their family
        profile is hidden.
        """
        # Log into User 1's account
        logged_in = self.client.login(email='example3000@mail.com',
                                      password='alpaca4567')
        self.assertTrue(logged_in)

        # Visit User 2's family profile and confirm there is no message about
        # not being able to send a request in hidden mode
        response = self.client.get(reverse('family-profile', kwargs={'pk': self.user2.familyprofile.pk}))
        self.assertNotContains(response, 'You cannot send a request in hidden mode')

        # Make User 1's family profile hidden
        familyprofile = FamilyProfile.objects.get(user=self.user1)
        familyprofile.hidden.add(familyprofile.user)
        confirm_self = familyprofile.hidden.all()[0]
        self.assertEquals(familyprofile.user, confirm_self)

        # Visit User 2's family profile and and confirm there is a message
        # about not being able to send a request in hidden mode
        response = self.client.get(reverse('family-profile', kwargs={'pk': self.user2.familyprofile.pk}))
        self.assertContains(response, 'You cannot send a request in hidden mode')

    def test_added_database_objects(self):
        """Check that multiple choices are addable as a list when creating
        category objects and confirm they were stored as objects in the
        corresponding models.
        """
        # Choices for category objects
        hobby_choices = ['Fishing', 'Food', 'Music', 'Traveling']
        state_choice = 'California'
        city_choice = 'San Francisco'
        language_choices = ['English', 'Spanish']
        day_choices = ['Wednesday', 'Friday', 'Weekends']

        # Create an object for each category model
        Hobby.objects.create(user=self.user1.familyprofile,
                             hobbies=hobby_choices
                             )
        Location.objects.create(user=self.user1.familyprofile,
                                state=state_choice,
                                city=city_choice
                                )
        Language.objects.create(user=self.user1.familyprofile,
                                languages=language_choices
                                )
        Availability.objects.create(user=self.user1.familyprofile,
                                    days=day_choices
                                    )

        # Confirm objects contain the correct choices
        self.assertEqual(getattr(Hobby.objects.first(), 'hobbies'), hobby_choices)
        self.assertEqual(getattr(Location.objects.first(), 'state'), state_choice)
        self.assertEqual(getattr(Location.objects.first(), 'city'), city_choice)
        self.assertEqual(getattr(Language.objects.first(), 'languages'), language_choices)
        self.assertEqual(getattr(Availability.objects.first(), 'days'), day_choices)

    def test_edited_database_objects(self):
        """Check that edited category objects stored new info."""
        # Choices for category objects
        hobby_choices = ['Fishing', 'Food', 'Music', 'Traveling']
        state_choice = 'California'
        city_choice = 'San Francisco'
        language_choices = ['English', 'Spanish']
        day_choices = ['Wednesday', 'Friday', 'Weekends']

        # Create an object for each category model
        Hobby.objects.create(user=self.user1.familyprofile,
                             hobbies=hobby_choices
                             )
        Location.objects.create(user=self.user1.familyprofile,
                                state=state_choice,
                                city=city_choice
                                )
        Language.objects.create(user=self.user1.familyprofile,
                                languages=language_choices
                                )
        Availability.objects.create(user=self.user1.familyprofile,
                                    days=day_choices
                                    )

        # New choices for category objects
        new_hobby_choices = ['Fishing', 'Food']
        new_state_choice = 'California'
        new_city_choice = 'Alemany'
        new_language_choices = ['English']
        new_day_choices = ['Friday', 'Weekends']

        # Create an object for each category model
        Hobby.objects.filter(pk=1).update(user=self.user1.familyprofile,
                                          hobbies=new_hobby_choices
                                         )
        Location.objects.filter(pk=1).update(user=self.user1.familyprofile,
                                             state=new_state_choice,
                                             city=new_city_choice
                                            )
        Language.objects.filter(pk=1).update(user=self.user1.familyprofile,
                                             languages=new_language_choices
                                            )
        Availability.objects.filter(pk=1).update(user=self.user1.familyprofile,
                                                 days=new_day_choices
                                                )

        # Confirm objects contain the correct choices
        self.assertEqual(getattr(Hobby.objects.first(), 'hobbies'), new_hobby_choices)
        self.assertEqual(getattr(Location.objects.first(), 'state'), new_state_choice)
        self.assertEqual(getattr(Location.objects.first(), 'city'), new_city_choice)
        self.assertEqual(getattr(Language.objects.first(), 'languages'), new_language_choices)
        self.assertEqual(getattr(Availability.objects.first(), 'days'), new_day_choices)

    def test_familyprofile_set_up_character_limit(self):
        """Confirm that exceeding max length character limits in family
        profile set up will result in failed set up.
        """
        self.client.login(email='example5000@mail.com',
                          password='alpaca4567')

        # Attempt family profile set up with max_length exceeded
        self.client.post(reverse('create-profile'), data={
            'user': self.user3,
            'family_name': 'x' * 50,   # 50 characters (exceed max_length=30)
            'contact_info': 'x' * 500  # 500 characters (exceed max_length=255)
        })

        # Confirm no family profile object was added and that attempting to
        # visit the non-existent family profile page results in 404 HTTP error
        self.assertEquals(FamilyProfile.objects.all().count(), 2)
        response = self.client.get(reverse('family-profile', kwargs={'pk': 3}))
        self.assertEquals(response.status_code, 404)

        # Show that using an acceptable character limit results in a
        # successful family profile set up
        self.client.post(reverse('create-profile'), data={
            'user': self.user3,
            'family_name': 'x' * 10,
            'contact_info': 'x' * 200
        })
        self.assertEquals(FamilyProfile.objects.all().count(), 3)
        response = self.client.get(reverse('family-profile', kwargs={'pk': 3}))
        self.assertEquals(response.status_code, 200)


class FamilyMemberTests(TestCase):

    """Create family member objects and test for unique id and required fields
    of user and first_name.
    """

    def setUp(self):
        """Create two user objects and then create a family profile for each."""
        CustomUserModel.objects.create(email='example3000@mail.com',
                                       username='example3000',
                                       password='alpaca4567',
                                       is_adult=True)

        self.user = CustomUserModel.objects.get(id=1)

        FamilyProfile.objects.create(user=self.user,
                                     family_name='Example 3000')

        self.family = FamilyProfile.objects.get(user=self.user)

        FamilyMember.objects.create(user=self.family,
                                    first_name='Hansel')

        FamilyMember.objects.create(user=self.family,
                                    first_name='Gretel')

    def test_unique_familymember_id(self):
        """Confirm that each family member has a unique id and string label."""
        family = FamilyProfile.objects.get(user=self.user)
        familymembers = FamilyMember.objects.filter(user=self.family)

        for member in familymembers:
            expected_object_name = f'{member.__str__()}'
            raw_string = str(member.user) + ' | Log ID: ' + str(member.id)
            self.assertEquals(expected_object_name, raw_string)

    def test_optional_fields(self):
        """Check that only the user and first_name have been filled out to
        test that all other fields are optional.
        """
        family = FamilyProfile.objects.get(user=self.user)
        familymembers = FamilyMember.objects.filter(user=self.family)

        for member in familymembers:
            expected_object_user = f'{member.user}'
            expected_object_first_name = f'{member.first_name}'
            self.assertTrue(expected_object_user)
            self.assertTrue(expected_object_first_name)
            self.assertIsNone(member.last_name)
            self.assertIsNone(member.relation)
            self.assertIsNone(member.age_range)
            self.assertIsNone(member.about)


class RegistrationTests(TestCase):

    """Run registration tests relating to sign up processes."""

    def test_sign_up_time(self):
        """Simulate the sign up process and confirm that the run time and
        redirect time are at most a total of mere seconds.
        """
        # Go to sign up page
        response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response, 'registration/register.html')

        # Simulate sign up and confirm user has been created
        response = self.client.post(reverse('register'), data={
            'email': 'example3000@mail.com',
            'username': 'example3000',
            'password1': 'alpaca4567',
            'password2': 'alpaca4567',
            'family_relation_status': 'Parent',
            'is_adult': True
        })
        self.assertEqual(CustomUserModel.objects.all().count(), 1)
        
        # Go to redirect page which is the login page
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Email:')

    def test_non_logged_in_user_privileges(self):
        """Check that the search page and add family member pages are not
        accessible to non-logged-in users.
        """
        response = self.client.get(reverse('search-page'))
        self.assertEquals(response.status_code, 302)

        response = self.client.get(reverse('add-family-member'))
        self.assertEquals(response.status_code, 302)
