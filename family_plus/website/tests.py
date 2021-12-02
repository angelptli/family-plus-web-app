from django.test import TestCase, SimpleTestCase
from django.urls import reverse


from custom_user_model.models import CustomUserModel
from website import views


class WelcomePageTests(SimpleTestCase):

    """Test for the correct status code, content, and templates used in
    the welcome page.
    """

    def test_welcome_page_status_code(self):
        """Test that the welcome page exists and returns a HTTP 200 OK
        success status responses code to indicate the request has succeeded."""
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
    the home page."""

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

    """Create a user and test that authentication log in works."""

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