from django.test import TestCase, SimpleTestCase
from django.urls import reverse

from custom_user_model.models import CustomUserModel


class WelcomePageTests(SimpleTestCase):

    """Test for the correct status code, content, and templates used in
    the welcome page.

    Inspired by: https://learndjango.com/tutorials/django-testing-tutorial
    Learned how to write basic unit tests.
    """

    def test_welcome_page_status_code(self):
        """Test that the welcome page exists and returns a HTTP 200 OK
        success status responses code to indicate the request has succeeded.
        """
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        """Confirm the welcome page uses the url named welcome."""
        response = self.client.get(reverse('welcome'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Check that the three templates used in the welcome page are
        welcome.html, base.html, and navbar.html."""
        response = self.client.get(reverse('welcome'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page/welcome.html')
        self.assertTemplateUsed(response, 'header_footer/base.html')
        self.assertTemplateUsed(response, 'header_footer/navbar.html')

    def test_welcome_page_contains_correct_html(self):
        """Confirm that the HTML contains the description titles."""
        response = self.client.get('/')
        self.assertContains(response, 'Add More Members To Your Family')
        self.assertContains(response, 'Get To Know Others Like You')
        self.assertContains(response, 'Learn A New Hobby And')

    def test_welcome_page_does_not_contain_incorrect_html(self):
        """Check that no button or description contains the words
        'Family Profile'. The family profile buttons should only be found
        in the navbar menu and home page."""
        response = self.client.get('/')
        self.assertNotContains(response, 'Family Profile')


class HomePageTests(SimpleTestCase):

    """Test for the correct status code, content, and templates used in
    the home page.

    Inspired by: https://learndjango.com/tutorials/django-testing-tutorial
    Learned how to write basic unit tests.
    """

    def test_home_page_status_code(self):
        """Test that the welcome page exists and returns a HTTP 200 OK
        success status responses code to indicate the request has succeeded."""
        response = self.client.get('/home/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        """Confirm the home page uses the url named home."""
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """Check that the three templates used in the home page are
        home.html, base.html, and navbar.html."""
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home_page/home.html')
        self.assertTemplateUsed(response, 'header_footer/base.html')
        self.assertTemplateUsed(response, 'header_footer/navbar.html')

    def test_home_page_contains_correct_html(self):
        """Confirm that the HTML contains the website's name as a title."""
        response = self.client.get('/home/')
        self.assertContains(response, 'Family+')

    def test_home_page_does_not_contain_incorrect_html(self):
        """Check that no button or description contains the words 'Welcome'."""
        response = self.client.get('/home/')
        self.assertNotContains(response, 'Welcome')


class AuthenticationTests(TestCase):

    """Test that users authentication and redirection logged in versions of
    pages.
    """

    def setUp(self):
        """Create two user objects and then create a family profile for each."""
        CustomUserModel.objects.create(email='example3000@mail.com',
                                       username='example3000',
                                       is_adult=True)

        self.user = CustomUserModel.objects.get(id=1)

        # Set password
        self.user.set_password('alpaca4567')
        self.user.save()

    def test_authentication(self):
        """Check that a user can log in."""
        logged_in = self.client.login(email='example3000@mail.com',
                                      password='alpaca4567')
        self.assertTrue(logged_in)

    def test_logged_in_redirect(self):
        """Confirm that a user is brought to the home page instead of the
        welcome page when logged in.
        """
        # Go to home page and confirm it is the version for logged out users
        response = self.client.get(reverse('welcome'))
        self.assertContains(response, 'Login')
        self.assertContains(response, 'Sign Up')

        # Go to welcome page and confirm it is the correct page
        response = self.client.get(reverse('welcome'))
        self.assertContains(response, 'Welcome to Family+')

        # Go to login page and confirm it is the correct page
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'Email:')
        self.assertContains(response, 'Password:')

        # Log in and confirm user is logged in
        logged_in = self.client.login(email='example3000@mail.com',
                                      password='alpaca4567')
        self.assertTrue(logged_in)

        # Go to welcome page and confirm a home page redirection by checking
        # for strings only located in the home page for logged in users
        response = self.client.get(reverse('welcome'))
        self.assertContains(response, 'Search')
        self.assertContains(response, 'My Family Profile')
        self.assertContains(response, 'Logout')
