from django.test import TestCase

from custom_user_model.models import CustomUserModel
from website_users.models import FamilyProfile, FamilyMember


class FamilyProfileTests(TestCase):

    """Create users and a family profile for each to perform tests. Test that
    each family profile has been created properly, that a profile picture is
    optional, and the correct family bio is saved when updated.
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

