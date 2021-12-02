from django.test import TestCase

from custom_user_model.models import CustomUserModel


class UserTests(TestCase):

    """Create users and confirm that they they meet the minimum age
    requirement to sign up (18 years old or over).
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

    def test_is_adult_status(self):
        """Check that each user is an adult at least 18 years old or over."""
        expected_object_name1 = f'{self.user1.is_adult}'
        expected_object_name2 = f'{self.user2.is_adult}'
        self.assertEquals(expected_object_name1, 'True')
        self.assertEquals(expected_object_name2, 'True')

    def test_unique_users(self):
        """Confirm users have unique usernames."""
        expected_object_name1 = f'{self.user1.username}'
        expected_object_name2 = f'{self.user2.username}'
        self.assertNotEquals(expected_object_name1, expected_object_name2)